from django.db import models
# from django.db.models.fields import SmallIntegerField
import django.contrib.auth

class Report(models.Model):
    """
    Класс для создания отчетов.
    """
    
    # Fields
    field_name = "Отчет от "
    publication_date = models.DateTimeField
    production_department = models.BigIntegerField(verbose_name='Номер производственного отделения', default=0)
    greenhouse = models.BigIntegerField(verbose_name='Номер теплицы', default=0)
    report_comment = models.CharField(verbose_name='Комментарий к отчету', max_length=255)
    

    # Methods
    def __str__(self):
        return self.field_name
    

    # Metadata
    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"

    
    # def get_absolute_url(self):
         #"""
         #Returns the url to access a particular instance of MyModelName.
         #"""
         #return reverse('model-detail-view', args=[str(self.id)])


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
        ordering = ["-url"]
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    # Methods
    def __str__(self):
        return self.field_name + self.url