from django.db import models

class Report(models.Model):
    """
    Класс для создания отчетов.
    """
    
    # Fields
    publication_date = models.DateTimeField(verbose_name='Дата создания отчета')
    production_department = models.BigIntegerField(verbose_name='Номер производственного отделения', default=0)
    greenhouse = models.BigIntegerField(verbose_name='Номер теплицы', default=0)
    report_comment = models.CharField(verbose_name='Комментарий к отчету', max_length=255)
    
    
    # Metadata
    # class Meta:
        # ordering = ["-my_field_name"]

    # Methods
    # def get_absolute_url(self):
         #"""
         #Returns the url to access a particular instance of MyModelName.
         #"""
         #return reverse('model-detail-view', args=[str(self.id)])

    #def __str__(self):
        #"""
        #String for representing the MyModelName object (in Admin site etc.)
        #"""
        #return self.field_name