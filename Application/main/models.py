from django.db import models

class Report(models.Model):
    report_comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField('Дата создания отчета')