from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import DecimalField
import decimal
# from django.db.models.fields import SmallIntegerField
# import django.contrib.auth


class Menu(models.Model):
    """
    """

    # Fields
    field_name = "Меню для "
    url = models.CharField(verbose_name='Применяется к странице', max_length=255)
    # items = models.ArrayField(
    #     models.CharField(max_length=15, blank=True, verbose_name='Название пункта'),
    #     size=8,
    #     verbose_name='Пункты меню'
    # )
    # items = models.JSONField(verbose_name='Пункты меню', default=dict)

    # Metadata
    class Meta:
        # ordering = ["-url"]
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    # Methods
    def __str__(self):
        return self.field_name + self.url


# Таблицы выбора
class Cultures(models.Model):
    """
    """

    # Fields
    culture_name = models.CharField(verbose_name='Название культуры', max_length=50, primary_key=True)

    # Metadata
    class Meta:
        verbose_name = "Культуру"
        verbose_name_plural = "Культуры"

    # Methods
    def __str__(self):
        return self.culture_name


class GrowthStages(models.Model):
    """
    """

    # Fields
    growth_stage = models.CharField(verbose_name='Стадия роста', max_length=100, primary_key=True)

    # Metadata
    class Meta:
        verbose_name = "Стадия роста"
        verbose_name_plural = "Стадии роста"

    # Methods
    def __str__(self):
        return self.growth_stage


# Модель отчета
class Report(models.Model):
    """
    Класс для создания отчетов.
    """


    # Методы
    def __str__(self):
        """Описание экземпляра модели в панели админа"""
        return "Отчет №" + str(self.id) + " от " + str(self.measurement_date.day) + "." + str(self.measurement_date.month) + "." + str(self.measurement_date.year) + " (Теплица №" + str(self.greenhouse) + ")"
    
    # Проверка работы функций
    # def __str__(self):
    #     return "Приход ФАР за 1 час от системы досвечивания: " + str(self.PAR_for_hour_from_lighting_system) + ", Приход ФАР/сут от системы досвечивания: " + str(self.PAR_per_day_from_lighting_system) + ", Суммарная ФАР с досветкой: " + str(self.PAR_total) + ", дельта Тд-Тн: " + str(self.temp_delta) + ", дельта ОВВн- ОВВд: " + str(self.RH_delta) + ", Вылито воды на мл/Дж: " + str(self.water_per_ml_j) + ", Длина междоузлия: " + str(self.internode_length) + ", Индекс листовой пластинки: " + str(self.leaf_blade_index)
    
    def getPARPerHour(self):
        """Функция определяющая количество фотосинтетически активной радиации в час по мощности системы досвечивания"""
        values_dict = {
            23000: 82,
            22000: 79,
            21000: 75,
            20000: 71,
            19000: 68,
            18000: 64,
            17000: 61,
            16000: 57,
            15500: 55
        }

        return values_dict.get(self.lighting_system_power, 0)


    def getPARPerDay(self):
        return self.PAR_for_hour_from_lighting_system * self.lighting_system_operating_time

    
    def getTotalPAR(self):
        return round(self.solar_radiation_per_day * decimal.Decimal(self.glazing_throughput / 100) + self.PAR_per_day_from_lighting_system, 2)
    

    def getTempDelta(self):
        return self.temp_day - self.temp_night

    def getPHDelta(self):
        return self.RH_night - self.RH_day

    def getWaterPerMlJ(self):
        return round(self.water_per_plant * decimal.Decimal(3.8) / self.PAR_total, 2)

    def getInternodeLength(self):
        return round(self.growth_week / self.internode_number, 2)

    def getLeafBladeIndex(self):
        return round((self.leaves_total_number * self.leaf_blade_length * self.leaf_blade_width * decimal.Decimal(3.8 * 0.7)) / decimal.Decimal(10000), 2)


    # Поля модели
    # -- Заглавная часть --
    measurement_date = models.DateField(verbose_name='Дата замера')
    production_department = models.PositiveIntegerField(verbose_name='Номер производственного отделения')
    greenhouse = models.PositiveIntegerField(verbose_name='Номер теплицы')
    culture = models.ForeignKey(Cultures, on_delete=models.CASCADE, verbose_name='Культура / гибрид')
    growth_stage = models.ForeignKey(GrowthStages, on_delete=models.CASCADE, verbose_name='Стадия роста')
    report_comment = models.CharField(verbose_name='Комментарий к отчету', max_length=255, blank=True)

    # -- Обеспеченность растений светом --
    solar_radiation_per_day = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Приход естественной солнечной радиации за сутки')
    light_intensity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Интенсивность естественного света')
    light_intensity_per_day = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Интенсивность естественного света (за световой день)')
    glazing_throughput = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)], verbose_name='Пропускная способность остекления (в процентах)')
    time_sunrise = models.TimeField(verbose_name='Время естественного восхода Солнца')
    time_sunset = models.TimeField(verbose_name='Время естественного захода Солнца')
    lighting_system_power = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Мощность системы досвечивания')
    lighting_system_turn_on_time = models.TimeField(verbose_name='Время включения досвечивания')
    lighting_system_turn_off_time = models.TimeField(verbose_name='Время отключения досвечивания')
    lighting_system_operating_time = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)], verbose_name='Количество часов работы системы досвечивания (50% вкл и откл берутся как 0,5 за 1 полный час)')
    unlit_light_points = models.PositiveIntegerField(verbose_name='Количество негорящих светоточек')
    PAR_for_hour_from_lighting_system = property(getPARPerHour) # Приход ФАР за 1 час от системы досвечивания
    PAR_per_day_from_lighting_system = property(getPARPerDay) # Приход ФАР/сут от системы досвечивания
    PAR_total = property(getTotalPAR) # Суммарная ФАР с досветкой

    # -- Микроклимат растений --
    temp_day = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Т дневная')
    temp_night = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Т ночная')
    temp_day_max = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Т макс дневная')
    temp_delta = property(getTempDelta) # дельта Тд-Тн
    temp_day_avr = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Т среднесуточная')
    CO2_avg_concentration_per_day = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Средняя концентрация в течении светового дня СО2')
    CO2_maximum_supply = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Макс. подача СО2')
    CO2_start_time_supply = models.TimeField(verbose_name='Время начала подачи СО2')
    CO2_end_time_supply = models.TimeField(verbose_name='Время окончания подачи СО2')
    gas_measurements_nitrogen_oxide = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Замеры отходящих газов с котельной - Окись Азота')
    gas_measurements_nitrogen_dioxide = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Замеры отходящих газов с котельной - Азота диоксид')
    gas_measurements_carbon_monoxide = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Замеры отходящих газов с котельной - Угарный газ')
    RH_day = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)], verbose_name='ОВВ дневная')
    RH_night = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)], verbose_name='ОВВ ночная')
    RH_delta = property(getPHDelta) # дельта ОВВн- ОВВд
    DVP = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='ДВП')

    # -- Полив растений --
    water_mixer_EC = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='EC поливной воды на миксере')
    water_mixer_temp = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Т поливной воды на миксере')
    water_dropper_temp = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Т поливной воды из под капельницы')
    substrate_temp = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Т субстрата')
    watering_start_time = models.TimeField(verbose_name='Начало полива')
    watering_end_time = models.TimeField(verbose_name='Конец полива')
    water_per_plant = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Вылито воды на 1 растение')
    water_per_ml_j = property(getWaterPerMlJ) # Вылито воды на мл/Дж
    drainage = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)], verbose_name='Дренаж')
    water_availability = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)], verbose_name='Водообеспеченность на начало текущего дня')
    EC_irrigation = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='EC поливное')
    EC_substrate = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='EC в субстрате')
    PH_irrigation = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Ph поливное')
    PH_mat = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Ph  в мате')
    weight_loss_substrate = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)], verbose_name='Потеря веса в субстрате между циклами')
    weight_loss_mat = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)], verbose_name='Потеря веса мата за ночь (ночная усушка)')

    # -- Фенология растений --
    growth_week = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Прирост за неделю')
    leaves_new_number = models.PositiveIntegerField(verbose_name='Количество новых листьев')
    total_plants_length = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Общая длина растений')
    internode_length = property(getInternodeLength) # Длина междоузлия
    internode_number = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Число междоузлиев')
    crown_diameter = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Диаметр макушки')
    stem_diameter = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Диаметр стебля')
    leaves_total_number = models.PositiveIntegerField(verbose_name='Количество листьев на растении')
    leaf_blade_length = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Длина листа')
    leaf_blade_width = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Ширина листа')
    leaf_blade_index = property(getLeafBladeIndex) # Индекс листовой пластинки
    flowering_plants_number = models.PositiveIntegerField(verbose_name='Количество цветущих')
    fruits_on_plant = models.PositiveIntegerField(verbose_name='Количество плодов на растении')
    fruit_avg_weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Средний вес плод')
    week_harvest = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Урожай за неделю')
    non_standard_products_percentage = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)], verbose_name='% нестандартной продукции')

    # -- Анализы  агрохимлаборатории (анализы проводятся лаборантом и агрохимиком) --
    electrical_conductivity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Электропроводность')
    total_alkalinity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Общая щелочность')
    calcium = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Кальций')
    magnesium = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Магний')
    sodium = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Натрий')
    chlorides = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Хлориды')
    nutrient_solution_nitrate_nitrogen = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Содержание нитратного азота в питательном растворе')
    nutrient_solution_phosphorus = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Содержание фосфора в питательном растворе')
    nutrient_solution_potassium = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Содержание калия в питательном растворе')
    nutrient_solution_calcium = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Содержание кальция в питательном растворе')
    nutrient_solution_magnesium = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Содержание магния в питательном растворе')
    nutrient_solution_chlorine = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], verbose_name='Содержание хлора в питательном растворе')

    # -- Защита растений --
    disease_infection = models.PositiveIntegerField(verbose_name='Зараженность болезнями')
    disease_infection_virus = models.PositiveIntegerField(verbose_name='Зараженность болезнями: ВЗКМО, вирусы, бактериозы')
    disease_infection_vermin = models.PositiveIntegerField(verbose_name='Зараженность вредителями: белокрылка, тля трипс')
    disease_infection_trips = models.PositiveIntegerField(verbose_name='Зараженность вредителями: ЗЦ трипс')
    foliar_treatments = models.PositiveIntegerField(verbose_name='Внекорневые обработки')
    chemical_treatment = models.PositiveIntegerField(verbose_name='Химобработки совместимые')
    pollination = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)], verbose_name='Опыление')




    # Метадата
    class Meta:
        ordering = ['greenhouse', 'measurement_date']
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"

    
    # def get_absolute_url(self):
         #"""
         #Returns the url to access a particular instance of MyModelName.
         #"""
         #return reverse('model-detail-view', args=[str(self.id)])