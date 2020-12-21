from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from SARZS.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('show', show, name='show'),
    path('check/<int:id>', check, name='check'),
    path('check/result/<int:id>', result, name='result'),

    #path('register', registerPage, name="register"),
    #path('login', loginPage, name="login"),
    path('logout', logoutUser, name="logout"),

    path('hospitals', hospital, name='hospital'),
    path('hospitalDetails/<int:id>', hospitalDetails, name='hospitalDetails'),
    path('hospitalRating/<int:id>', hospitalRating, name='hospitalRating'),
    path('hospitalComment/<int:id>', hospitalComment, name='hospitalComment'),

    path('diagnostic_center', diagnostic_center, name='diagnostic_center'),
    path('diagnosticDetails/<int:id>', diagnosticDetails, name='diagnosticDetails'),
    path('diagnosticRating/<int:id>', diagnosticRating, name='diagnosticRating'),
    path('diagnosticComment/<int:id>', diagnosticComment, name='diagnosticComment'),

    path('BMI', BMI, name="BMI"),
    path('growth', growth, name='growth'),

    path('doctor', doctor, name='doctor'),
    path('doctorDetails/<int:id>', doctorDetails, name='doctorDetails'),
    path('doctorRating/<int:id>', doctorRating, name='doctorRating'),
    path('doctorComment/<int:id>', doctorComment, name='doctorComment'),
    path('alldoctors', alldoctors, name='alldoctors'),
    path('recordDoctor/<int:id>', recordDoctor, name='recordDoctor'),

    url(r'^login/$', loginPage, name='login'),
    url(r'^register/$', registerPage, name="register"),

    url(r'^via/$', via, name='via'),
    url(r'^via_login/$', via_login, name='via_login'),
    url(r'^via_register/$', via_register, name='via_register'),

    url(r'^save_record/$', save_record, name='save_record'),
    url(r'^records/$', records, name='records'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^profileUpdate/$', profileUpdate, name='profileUpdate'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="htmls/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="htmls/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="htmls/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="htmls/password_reset_done.html"),
        name="password_reset_complete"),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="htmls/change_password.html"), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="htmls/password_change_done.html"), name='password_change_done'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
