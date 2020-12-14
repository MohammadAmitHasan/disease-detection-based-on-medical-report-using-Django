from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .filters import *
from .forms import *
from .models import *

def home(request):
    return render(request,'htmls/home.html')

def show(request):
    table_test = test.objects.all().order_by("Test_Name")
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
        comment = row.Test_Name + " label is low"
        record_comment = row.Test_Name + " label was low"
        suggetions = row.tlow_advice
        disease_name = row.tlow_disease

    elif value > row.tmax:
        comment = row.Test_Name + " label is high"
        record_comment = row.Test_Name + " label was high"
        suggetions = row.thigh_advice
        disease_name = row.thigh_disease
    else:
        comment = row.Test_Name + " label is normal"
        record_comment = row.Test_Name + " label was normal"

    global Test_Name, tlevel, treference, rcomment

    def Test_Name():
        return row.Test_Name
    def tlevel():
        return value
    def treference():
        return row.treference
    def rcomment():
        return record_comment

    return render(request,'htmls/result.html', {'row': row, 'comment': comment, 'suggetions': suggetions, 'disease_name': disease_name})

def registerPage(request):
    a = ''
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user = form.cleaned_data.get('username')
            if 'next' in request.POST:
                a = request.POST.get('next')
                messages.success(request, f'Account has created successfully for ' + user)
                return redirect(request.POST.get('next'))
            messages.success(request, f'Account has created successfully for ' + user)
            return redirect('home')

    return render(request, 'htmls/register.html', {'form': form, 'a': a})

def loginPage(request):
    a = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                a = request.POST.get('next')
                messages.success(request, f'Loged in successfully for '+ user.username)
                return redirect(request.POST.get('next'))
            else:
                messages.success(request, f'Loged in successfully for '+ user.username)
                return redirect('home')
        else:
            messages.info(request, 'Username or password is wrong')
    return render(request, 'htmls/login.html',{'a': a})

def logoutUser(request):
    logout(request)
    messages.success(request, f'Loged out successfully')
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
            bmi_comment = "You have Overweight"
        elif (BMI >= 30 and BMI < 35):
            bmi_comment = "You have Obese Class I"
        elif (BMI >= 35 and BMI < 40):
            bmi_comment = "You have Obese Class II"
        else:
            bmi_comment = "You have Obese Class III"

    return render(request, 'htmls/BMI.html', {'bmi_result': bmi_result, 'bmi_comment': bmi_comment})

def growth(request):
    return render(request, 'htmls/growth.html')

@login_required(login_url='via')
def doctor(request):
    #doctor_dept = request.session['result_doctor']
    doctor_dept = result_doctor()
    special_doctor = doctor_list.objects.filter(Department__icontains=doctor_dept)
    myFilter = doctorFilter(request.GET, queryset=special_doctor)
    special_doctor = myFilter.qs
    return render(request, 'htmls/doctor.html', {'doctor_dept': doctor_dept, 'special_doctor': special_doctor, 'myFilter': myFilter})

@login_required(login_url='via')
def recordDoctor(request, id):
    doctor = record.objects.get(id=id)
    special_doctor = doctor_list.objects.filter(Department__icontains=doctor.tdoctor)
    myFilter = doctorFilter(request.GET, queryset=special_doctor)
    special_doctor = myFilter.qs

    return render(request, 'htmls/doctor.html', {'doctor_dept': doctor.tdoctor, 'special_doctor': special_doctor, 'myFilter': myFilter})

@login_required(login_url='via')
def alldoctors(request):
    doctor_dept = "Expert Doctors"
    special_doctor = doctor_list.objects.all()
    myFilter = alldoctorFilter(request.GET, queryset=special_doctor)
    special_doctor = myFilter.qs
    return render(request, 'htmls/doctor.html', {'doctor_dept': doctor_dept, 'special_doctor': special_doctor, 'myFilter': myFilter})

def via(request):
    return render(request, 'htmls/via.html')

def via_login(request):
    a = ''
    if request.method == 'POST':
        if 'next' in request.POST:
            a = request.POST.get('next')
            return render(request, 'htmls/login.html', {'a': a})
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
    userid = User.objects.get(username=request.user)
    Record = record()
    if request.user.is_authenticated:
        Record.rid = userid.id
        Record.Test_Name = Test_Name()
        Record.tlevel = tlevel()
        Record.treference = treference()
        Record.rcomment = rcomment()
        Record.tdoctor = result_doctor()
        Record.save()
    return redirect('records')

@login_required(login_url='via')
def records(request):
    userid = User.objects.get(username=request.user)
    if request.user.is_authenticated:
        user_record = record.objects.filter(rid=userid.id).order_by("-rdate")
    return render(request, 'htmls/records.html', {'user_record': user_record})

@login_required(login_url='via')
def doctorDetails(request,id):

    doctor = doctor_list.objects.get(id=id)
    row = docReview.objects.filter(DOCid=doctor.DOCid).order_by("-date")

    return render(request, 'htmls/doctorReview.html', {'row':row, 'doctor': doctor})

@login_required(login_url='via')
def doctorRating(request,id):
    doctor = doctor_list.objects.get(id=id)
    if request.method == 'POST':
        ratings = float(request.POST['rating'])
        doctor.totalRating = doctor.totalRating + ratings
        doctor.numberOfRating += 1
        doctor.rating = round((doctor.totalRating/doctor.numberOfRating),2)
        print(doctor.rating)
        doctor.save()
    return redirect('doctorDetails',id)

@login_required(login_url='via')
def doctorComment(request,id):
    doctor = doctor_list.objects.get(id=id)
    comment_table = docReview()
    if request.method == 'POST':
        comments = request.POST['comment']
        comment_table.DOCid = doctor.DOCid
        comment_table.user = request.user
        comment_table.comment = comments
        comment_table.save()

    return redirect('doctorDetails',id)

@login_required(login_url='via')
def hospitalDetails(request,id):
    hospital = hospitals.objects.get(id=id)
    row = hospitalReview.objects.filter(Hid=hospital.Hid).order_by("-date")
    return render(request, 'htmls/HospitalReview.html', {'row': row, 'hospital': hospital})

@login_required(login_url='via')
def hospitalRating(request, id):
    hospital = hospitals.objects.get(id=id)
    if request.method == 'POST':
        ratings = float(request.POST['rating'])
        hospital.TotalRating = hospital.TotalRating + ratings
        hospital.numberOfRating += 1
        hospital.Rating = round((hospital.TotalRating/hospital.numberOfRating),2)
        hospital.save()
    return redirect('hospitalDetails',id)

@login_required(login_url='via')
def hospitalComment(request, id):
    hospital = hospitals.objects.get(id=id)
    comment_table = hospitalReview()
    if request.method == 'POST':
        comments = request.POST['comment']
        comment_table.Hid = hospital.Hid
        comment_table.user = request.user
        comment_table.comment = comments
        comment_table.save()

    return redirect('hospitalDetails', id)

@login_required(login_url='via')
def diagnosticDetails(request, id):
    diagnostic = diagnostic_centers.objects.get(id=id)
    row = diagnosticReview.objects.filter(Did=diagnostic.Did).order_by("-date")
    return render(request, 'htmls/DiagnosticReview.html', {'row':row, 'diagnostic': diagnostic})

@login_required(login_url='via')
def diagnosticRating(request, id):
    diagnostic = diagnostic_centers.objects.get(id=id)
    if request.method == 'POST':
        ratings = float(request.POST['rating'])
        diagnostic.TotalRating = diagnostic.TotalRating + ratings
        diagnostic.numberOfRating += 1
        diagnostic.Rating = round((diagnostic.TotalRating/diagnostic.numberOfRating), 2)
        diagnostic.save()
    return redirect('diagnosticDetails',id)

@login_required(login_url='via')
def diagnosticComment(request,id):
    diagnostic = diagnostic_centers.objects.get(id=id)
    comment_table = diagnosticReview()
    if request.method == 'POST':
        comments = request.POST['comment']
        comment_table.Did = diagnostic.Did
        comment_table.user = request.user
        comment_table.comment = comments
        comment_table.save()

    return redirect('diagnosticDetails',id)

@login_required(login_url='via')
def profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'htmls/profile.html', context)

@login_required(login_url='via')
def profileUpdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Account updated successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'htmls/profileUpdate.html',{'u_form': u_form})
