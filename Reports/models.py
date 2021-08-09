from django.db import models
# from django.db.models.fields import SmallIntegerField
import django.contrib.auth


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
    
    # Fields
    field_name = "Отчет №"
    measurement_date = models.DateField(verbose_name='Дата замера')
    production_department = models.PositiveIntegerField(verbose_name='Номер производственного отделения')
    greenhouse = models.PositiveIntegerField(verbose_name='Номер теплицы')
    culture = models.ForeignKey(Cultures, on_delete=models.CASCADE, verbose_name='Культура / гибрид')
    growth_stage = models.ForeignKey(GrowthStages, on_delete=models.CASCADE, verbose_name='Стадия роста')
    report_comment = models.CharField(verbose_name='Комментарий к отчету', max_length=255, blank=True)
    

    # Methods
    def __str__(self):
        return self.field_name + str(self.id) + " от " + str(self.measurement_date.day) + "." + str(self.measurement_date.month) + "." + str(self.measurement_date.year) + " (Теплица №" + str(self.greenhouse) + ")"
    

    # Metadata
    class Meta:
        ordering = ['greenhouse', 'measurement_date']
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"

    
    # def get_absolute_url(self):
         #"""
         #Returns the url to access a particular instance of MyModelName.
         #"""
         #return reverse('model-detail-view', args=[str(self.id)])