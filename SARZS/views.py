from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .filters import *


from .forms import CreateUserForm

def home(request):
    return render(request,'htmls/home.html')

def show(request):
    table_test = test.objects.all()

    myFilter = testFilter(request.GET, queryset=table_test)
    table_test = myFilter.qs

    return render(request, 'htmls/show.html', {'table_test': table_test, 'myFilter': myFilter})

def check(request,id):
    row = test.objects.get(id=id)
    return render(request, 'htmls/check.html', {'row': row})

def result(request,id):

    row = test.objects.get(id=id)
    value = float(request.POST['level'])
    record_comment = ''
    suggetions = ''
    disease_name = ''

    #request.session['result_doctor'] = row.tdoctor

    global result_doctor
    def result_doctor():
        return row.tdoctor

    if value < row.tmin:
        comment = "Your " + row.Test_Name + " label is low"
        record_comment = "Your " + row.Test_Name + " label was low"
        suggetions = row.tlow_advice
        disease_name = row.tlow_disease

    elif value > row.tmax:
        comment = "Your " + row.Test_Name + " label is high"
        record_comment = "Your " + row.Test_Name + " label was high"
        suggetions = row.thigh_advice
        disease_name = row.thigh_disease
    else:
        comment = "Your " + row.Test_Name + " label is normal"
        record_comment = "Your " + row.Test_Name + " label was normal"

    global Test_Name, tlevel, treference, rcomment

    def Test_Name():
        return row.Test_Name
    def tlevel():
        return value
    def treference():
        return row.treference
    def rcomment():
        return record_comment

    return render(request,'htmls/result.html', {'row': row,'comment': comment,'suggetions': suggetions, 'disease_name': disease_name})

def searchT(request):
    given_name = request.POST['name']
    table_test = test.objects.filter(Test_Name__icontains=given_name)
    return render(request, 'htmls/show.html', {'table_test': table_test, 'doctor': doctor})

def registerPage(request):
    a=''
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            if 'next' in request.POST:
                a = request.POST.get('next')
                return redirect(request.POST.get('next'))
            #user = form.cleaned_data.get('username')
            #messages.success(request, 'Account has created successfully for ' + user)
            return redirect('home')

    return render(request,'htmls/register.html', {'form': form, 'a': a})

def loginPage(request):
    a=''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                a = request.POST.get('next')
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            messages.info(request, 'Username or password is wrong')
    return render(request, 'htmls/login.html',{'a':a})

def logoutUser(request):
    logout(request)
    return redirect('home')

def hospital(request):
    hospital_list = hospitals.objects.all()

    myFilter = hospitalFilter(request.GET, queryset=hospital_list)
    hospital_list = myFilter.qs

    return render(request,'htmls/hospitals.html',{'hospital_list': hospital_list, 'myFilter': myFilter})

def diagnostic_center(request):
    diagnostic_list = diagnostic_centers.objects.all()

    myFilter = diagnostic_centerFilter(request.GET, queryset=diagnostic_list)
    diagnostic_list = myFilter.qs

    return render(request,'htmls/diagnostic_centers.html', {'diagnostic_list': diagnostic_list, 'myFilter': myFilter})

def BMI(request):
    bmi_result = ''
    bmi_comment = ''
    height = ''
    weight = ''
    
    if request.method == 'POST':
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])

        height = height * 0.0254
        BMI = weight/(height*height)
        bmi_result = "Your BMI is: " + "{:.2f}".format(BMI)

        if (BMI < 16):
            bmi_comment = "You have Severe Thinness"
        elif (BMI >= 16 and BMI < 17):
            bmi_comment = "You have Moderate Thinness"
        elif (BMI >= 17 and BMI <= 18.5):
            bmi_comment = "You have Mild Thinness"
        elif (BMI >= 18.5 and BMI < 25):
            bmi_comment = "You are normal"
        elif (BMI >= 25 and BMI < 30):
            bmi_comment = "You have Overweigh"
        elif (BMI >= 30 and BMI < 35):
            bmi_comment = "You have Obese Class I"
        elif (BMI >= 35 and BMI < 40):
            bmi_comment = "You have Obese Class II"
        else:
            bmi_comment = "You have Obese Class III"

    return render(request, 'htmls/BMI.html',{ 'bmi_result':bmi_result, 'bmi_comment': bmi_comment})

def growth(request):
    return render(request, 'htmls/growth.html')

@login_required(login_url='via')
def doctor(request):
    #doctor_dept = request.session['result_doctor']
    doctor_dept = result_doctor()
    special_doctor = doctor_list.objects.filter(tdoctor__icontains=doctor_dept)

    myFilter = doctorFilter(request.GET, queryset=special_doctor)
    special_doctor = myFilter.qs

    return render(request, 'htmls/doctor.html', {'doctor_dept': doctor_dept, 'special_doctor': special_doctor, 'myFilter': myFilter})


def via(request):
    return render(request, 'htmls/via.html')

def via_login(request):
    a = ''
    if request.method == 'POST':
        if 'next' in request.POST:
            a = request.POST.get('next')
            return render(request,'htmls/login.html',{'a':a})
    return render(request, 'htmls/via.html')

def via_register(request):
    a = ''
    form = CreateUserForm()
    if request.method == 'POST':
        if 'next' in request.POST:
            a = request.POST.get('next')
            return render(request,'htmls/register.html', {'form': form, 'a': a})
    return render(request, 'htmls/via.html')

@login_required(login_url='via')
def save_record(request):
    Record = record()
    if request.user.is_authenticated:
        Record.ruser = request.user
        Record.Test_Name = Test_Name()
        Record.tlevel = tlevel()
        Record.treference = treference()
        Record.rcomment = rcomment()
        Record.save()
    return redirect('profile')

@login_required(login_url='via')
def records(request):
    if request.user.is_authenticated:
        user_record = record.objects.filter(ruser=request.user)
    return render(request, 'htmls/records.html',{'user_record': user_record})