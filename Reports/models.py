from django.db import models

class Report(models.Model):
    """
    Класс для создания отчетов.
    """
    
    # Fields
    publication_date = models.DateTimeField
    production_department = models.BigIntegerField(verbose_name='Номер производственного отделения', default=0)
    greenhouse = models.BigIntegerField(verbose_name='Номер теплицы', default=0)
    report_comment = models.CharField(verbose_name='Комментарий к отчету', max_length=255)
    
    # Methods
    def __str__(self):
        return self.field_name
    
    # Metadata
    # class Meta:
        # ordering = ["-my_field_name"]

    
    # def get_absolute_url(self):
         #"""
         #Returns the url to access a particular instance of MyModelName.
         #"""
         #return reverse('model-detail-view', args=[str(self.id)])


class Menu(models.Model):
    """
    """

    # Fields
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

    # Methods
    def __str__(self):
        return self.field_name