from django.forms import ModelForm
from Reports.models import Report

# Create the form class.
class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = [field.name for field in model._meta.get_fields()]