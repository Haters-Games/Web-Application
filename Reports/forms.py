from django.forms import ModelForm
from Reports.models import Report

# Create the form class.
class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['measurement_date', 'production_department', 'greenhouse', 'culture', 'growth_stage']