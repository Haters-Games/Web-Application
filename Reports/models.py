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
        return self.field_name + str(self.id) + " от " + str(self.measurement_date.day) + "." + str(self.measurement_date.month) + "." + str(self.measurement_date.year) + " (Теплица №" + str(self.greenhouse) + ")"
    
    # def __str__(self):
    #     return 
    
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
        return(self.temp_day - self.temp_night)

    def getPHDelta(self):
        return(self.RH_day - self.RH_night)


    # Поля модели
    # -- Заглавная часть --
    field_name = "Отчет №"
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
    PAR_for_hour_from_lighting_system = property(getPARPerHour) # приход ФАР за 1 час от системы досвечивания
    PAR_per_day_from_lighting_system = property(getPARPerDay) # приход ФАР/сут от системы досвечивания
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