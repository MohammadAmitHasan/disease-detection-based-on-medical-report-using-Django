from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from SARZS.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('show', show, name='show'),
    path('check/<int:id>', check, name='check'),
    path('check/result/<int:id>', result,name='result'),
    
    path('searchT', searchT,name='searchT'),

    #path('register', registerPage, name="register"),
    #path('login', loginPage, name="login"),
    path('logout', logoutUser, name="logout"),

    path('hospitals', hospital, name='hospital'),
    path('diagnostic_center', diagnostic_center, name='diagnostic_center'),

    path('BMI', BMI, name="BMI"),
    path('growth', growth, name='growth'),

    path('doctor', doctor, name='doctor'),

    url(r'^login/$', loginPage, name='login'),
    url(r'^register/$', registerPage, name="register"),

    url(r'^via/$', via, name='via'),
    url(r'^via_login/$', via_login, name='via_login'),
    url(r'^via_register/$', via_register, name='via_register'),

    url(r'^save_record/$', save_record, name='save_record'),
    url(r'^records/$', records, name='records'),

]
