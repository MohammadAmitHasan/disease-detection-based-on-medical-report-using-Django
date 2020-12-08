import django_filters
from django_filters import CharFilter
from .models import *

class hospitalFilter(django_filters.FilterSet):
    Name = CharFilter(field_name='Name', lookup_expr='icontains')
    class Meta:
        model = hospitals
        #fields = '__all__'
        #exclude = ['Hid', 'Address', 'Contact', 'Website', 'Rating','TotalRating','numberOfRating','photo']
        fields = ['Name', 'Type', 'Area']

class diagnostic_centerFilter(django_filters.FilterSet):
    Name = CharFilter(field_name='Name', lookup_expr='icontains')
    class Meta:
        model = diagnostic_centers
        fields = ['Name', 'Type', 'Area']
        
class testFilter(django_filters.FilterSet):
    Test_Name = CharFilter(field_name='Test_Name', lookup_expr='icontains')
    class Meta:
        model = test
        fields = ['Test_Name']

class doctorFilter(django_filters.FilterSet):
    Name = CharFilter(field_name='Name', lookup_expr='icontains')
    class Meta:
        model = doctor_list
        fields = ['Name', 'Department', 'Area']
        

class alldoctorFilter(django_filters.FilterSet):
    Name = CharFilter(field_name='Name', lookup_expr='icontains')
    Department = CharFilter(field_name='Department', lookup_expr='icontains')
    class Meta:
        model = doctor_list
        fields = ['Name', 'Area']