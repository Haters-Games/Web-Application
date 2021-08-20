from django.db.models import fields
from django.forms import ModelForm
from django.db import models
from Reports.models import Report

class FullReport(ModelForm):
    class Meta:
        model = Report
        fields = [
            'measurement_date',
            'production_department', 
            'greenhouse', 
            'culture', 
            'growth_stage', 
            'report_comment',
            'solar_radiation_per_day',
            'light_intensity',
            'light_intensity_per_day',
            'glazing_throughput',
            'time_sunrise',
            'time_sunset',
            'lighting_system_power',
            'lighting_system_turn_on_time',
            'lighting_system_turn_off_time',
            'lighting_system_operating_time',
            'unlit_light_points',
            'temp_day',
            'temp_night',
            'temp_day_max',
            'temp_day_avr',
            'CO2_avg_concentration_per_day',
            'CO2_maximum_supply',
            'CO2_start_time_supply',
            'CO2_end_time_supply',
            'gas_measurements_nitrogen_oxide',
            'gas_measurements_nitrogen_dioxide',
            'gas_measurements_carbon_monoxide',
            'RH_day',
            'RH_night',
            'DVP',
            'water_mixer_EC',
            'water_mixer_temp',
            'water_dropper_temp',
            'substrate_temp',
            'watering_start_time',
            'watering_end_time',
            'water_per_plant',
            'drainage',
            'water_availability',
            'EC_irrigation',
            'EC_substrate',
            'PH_irrigation',
            'PH_mat',
            'weight_loss_substrate',
            'weight_loss_mat',
            'growth_week',
            'leaves_new_number',
            'total_plants_length',
            'internode_number',
            'crown_diameter',
            'stem_diameter',
            'leaves_total_number',
            'leaf_blade_length',
            'leaf_blade_width',
            'flowering_plants_number',
            'fruits_on_plant',
            'fruit_avg_weight',
            'week_harvest',
            'non_standard_products_percentage',
            'electrical_conductivity',
            'total_alkalinity',
            'calcium',
            'magnesium',
            'sodium',
            'chlorides',
            'nutrient_solution_nitrate_nitrogen',
            'nutrient_solution_phosphorus',
            'nutrient_solution_potassium',
            'nutrient_solution_calcium',
            'nutrient_solution_magnesium',
            'nutrient_solution_chlorine',
            'disease_infection',
            'disease_infection_virus',
            'disease_infection_vermin',
            'disease_infection_trips',
            'foliar_treatments',
            'chemical_treatment',
            'pollination']

# Create the form class.
class ReportMain(ModelForm):
    class Meta:
        model = Report
        fields = [
        'measurement_date',
        'production_department', 
        'greenhouse', 
        'culture', 
        'growth_stage', 
        'report_comment']
       
class ReportLight(ModelForm):
    class Meta:
        model = Report
        fields = [
        'solar_radiation_per_day',
        'light_intensity',
        'light_intensity_per_day',
        'glazing_throughput',
        'time_sunrise',
        'time_sunset',
        'lighting_system_power',
        'lighting_system_turn_on_time',
        'lighting_system_turn_off_time',
        'lighting_system_operating_time',
        'unlit_light_points']
        
class ReportMicroclimate(ModelForm):
    class Meta:
        model = Report
        fields = [
        'temp_day',
        'temp_night',
        'temp_day_max',
        'temp_day_avr',
        'CO2_avg_concentration_per_day',
        'CO2_maximum_supply',
        'CO2_start_time_supply',
        'CO2_end_time_supply',
        'gas_measurements_nitrogen_oxide',
        'gas_measurements_nitrogen_dioxide',
        'gas_measurements_carbon_monoxide',
        'RH_day',
        'RH_night',
        'DVP']

class ReportWatering(ModelForm):
    class Meta:
        model = Report
        fields = [
        'water_mixer_EC',
        'water_mixer_temp',
        'water_dropper_temp',
        'substrate_temp',
        'watering_start_time',
        'watering_end_time',
        'water_per_plant',
        'drainage',
        'water_availability',
        'EC_irrigation',
        'EC_substrate',
        'PH_irrigation',
        'PH_mat',
        'weight_loss_substrate',
        'weight_loss_mat']
        
class ReportPhenology(ModelForm):
    class Meta:
        model = Report
        fields = [
        'growth_week',
        'leaves_new_number',
        'total_plants_length',
        'internode_number',
        'crown_diameter',
        'stem_diameter',
        'leaves_total_number',
        'leaf_blade_length',
        'leaf_blade_width',
        'flowering_plants_number',
        'fruits_on_plant',
        'fruit_avg_weight',
        'week_harvest',
        'non_standard_products_percentage']

class ReportAnalyzes(ModelForm):
    class Meta:
        model = Report
        fields = [
        'electrical_conductivity',
        'total_alkalinity',
        'calcium',
        'magnesium',
        'sodium',
        'chlorides',
        'nutrient_solution_nitrate_nitrogen',
        'nutrient_solution_phosphorus',
        'nutrient_solution_potassium',
        'nutrient_solution_calcium',
        'nutrient_solution_magnesium',
        'nutrient_solution_chlorine']

class ReportProtection(ModelForm):
    class Meta:
        model = Report
        fields = [
        'disease_infection',
        'disease_infection_virus',
        'disease_infection_vermin',
        'disease_infection_trips',
        'foliar_treatments',
        'chemical_treatment',
        'pollination']