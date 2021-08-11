from django.db import models
from django.core.validators import MaxValueValidator
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
    solar_radiation_per_day = models.PositiveIntegerField(verbose_name='Приход естественной солнечной радиации за сутки')
    light_intensity = models.PositiveIntegerField(verbose_name='Интенсивность естественного света')
    light_intensity_per_day = models.PositiveIntegerField(verbose_name='Интенсивность естественного света (за световой день)')
    glazing_throughput = models.PositiveIntegerField(validators=[MaxValueValidator(100)], verbose_name='Пропускная способность остекления (в процентах)')
    sunrise_time = models.TimeField(verbose_name='Время естественного восхода Солнца')
    sunset_time = models.TimeField(verbose_name='Время естественного захода Солнца')
    lighting_system_power = models.PositiveIntegerField(verbose_name='Мощность системы досвечивания')
    lighting_system_turn_on_time = models.TimeField(verbose_name='Время включения досвечивания')
    lighting_system_turn_off_time = models.TimeField(verbose_name='Время отключения досвечивания')
    lighting_system_operating_time = models.PositiveIntegerField(verbose_name='Количество часов работы системы досвечивания (50% вкл и откл берутся как 0,5 за 1 полный час)')
    unlit_light_points = models.PositiveIntegerField(verbose_name='Количество негорящих светоточек')
    # PAR_for_hour_from_lighting_system = models.PositiveIntegerField(verbose_name='Приход ФАР за 1 час от системы досвечивания') - формула
    # PAR_per_day_from_lighting_system = models.PositiveIntegerField(verbose_name='Приход ФАР за 1 сутки от системы досвечивания') - формула
    # total_PAR = models.PositiveIntegerField(verbose_name='Суммарная ФАР с досветкой') - формула


    # Методы
    def __str__(self):
        return self.field_name + str(self.id) + " от " + str(self.measurement_date.day) + "." + str(self.measurement_date.month) + "." + str(self.measurement_date.year) + " (Теплица №" + str(self.greenhouse) + ")"
    

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