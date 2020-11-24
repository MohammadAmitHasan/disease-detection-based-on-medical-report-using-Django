import django_filters
from django_filters import CharFilter
from .models import *

class hospitalFilter(django_filters.FilterSet):
    Name = CharFilter(field_name='Name', lookup_expr='icontains')
    class Meta:
        model = hospitals
        fields = '__all__'
        exclude = ['Hid', 'Address', 'Contact', 'Website']

class diagnostic_centerFilter(django_filters.FilterSet):
    Name = CharFilter(field_name='Name', lookup_expr='icontains')
    class Meta:
        model = diagnostic_centers
        exclude = ['Did', 'Address', 'Contact', 'Website']

class testFilter(django_filters.FilterSet):
    Test_Name = CharFilter(field_name='Test_Name', lookup_expr='icontains')
    class Meta:
        model = test
        exclude = ['tid', 'tmin', 'tmax', 'treference', 'tunit', 'tdoctor', 'tdescription', 'thigh_disease', 'tlow_disease', 'thigh_advice', 'tlow_advice']

class doctorFilter(django_filters.FilterSet):
    Name = CharFilter(field_name='Name', lookup_expr='icontains')
    class Meta:
        model = doctor_list
        exclude = ['DOCid', 'Designation', 'Qualification', 'tdoctor','Contact','Address', 'Rating', 'TotalRating','NumRating']