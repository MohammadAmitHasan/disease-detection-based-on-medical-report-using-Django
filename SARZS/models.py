from django.db import models

class test(models.Model):
    tid = models.CharField(max_length=10, null=True)
    Test_Name = models.CharField(max_length=100, null=True)
    tmin = models.FloatField()
    tmax = models.FloatField()
    treference = models.CharField(max_length=100, null=True)
    tunit = models.CharField(max_length=100, null=True)
    tdoctor = models.CharField(max_length=100, null=True)
    tdescription = models.TextField(null=True)
    thigh_disease = models.CharField(max_length=100, null=True)
    tlow_disease = models.CharField(max_length=100, null=True)
    thigh_advice = models.TextField(null=True)
    tlow_advice = models.TextField(null=True)

class hospitals(models.Model):
    Hid = models.CharField(max_length=10, null=True)
    Name = models.CharField(max_length=200, null=True)
    type = (
        ('Government', 'Government'),
        ('Private','Private'),
    )
    Type = models.CharField(max_length=50, null=True, choices=type)
    Address = models.CharField(max_length=400, null=True)
    Contact = models.CharField(max_length=100, null=True)
    Website = models.CharField(max_length=100, null=True)
    division = (
        ('Barishal','Barishal '),
        ('Chittagong', 'Chittagong '),
        ('Dhaka', 'Dhaka'),
        ('Mymensingh', 'Mymensingh'),
        ('Khulna','Khulna'),
        ('Rajshahi', 'Rajshahi'),
        ('Rangpur', 'Rangpur'),
        ('Sylhet', 'Sylhet'),
    )
    Area = models.CharField(max_length=50, null=True, choices=division)

class diagnostic_centers(models.Model):
    Did = models.CharField(max_length=10, null=True)
    Name = models.CharField(max_length=200, null=True)
    type = (
        ('Government', 'Government'),
        ('Private', 'Private'),
    )
    Type = models.CharField(max_length=50, null=True, choices=type)
    Address = models.CharField(max_length=400, null=True)
    Contact = models.CharField(max_length=100, null=True)
    Website = models.CharField(max_length=100, null=True)
    division = (
        ('Barishal', 'Barishal '),
        ('Chittagong', 'Chittagong '),
        ('Dhaka', 'Dhaka'),
        ('Mymensingh', 'Mymensingh'),
        ('Khulna', 'Khulna'),
        ('Rajshahi', 'Rajshahi'),
        ('Rangpur', 'Rangpur'),
        ('Sylhet', 'Sylhet'),
    )
    Area = models.CharField(max_length=50, null=True, choices=division)

class doctor_list(models.Model):
    DOCid = models.CharField(max_length=10, null=True)
    Name = models.CharField(max_length=100, null=True)
    Designation = models.CharField(max_length=200, null=True)
    Qualification = models.CharField(max_length=200, null=True)
    tdoctor = models.CharField(max_length=200, null=True)
    Contact = models.CharField(max_length=200, null=True)
    Address = models.CharField(max_length=400, null=True)
    area = (
        ('Barishal', 'Barishal '),
        ('Chittagong', 'Chittagong '),
        ('Dhaka', 'Dhaka'),
        ('Mymensingh', 'Mymensingh'),
        ('Khulna', 'Khulna'),
        ('Rajshahi', 'Rajshahi'),
        ('Rangpur', 'Rangpur'),
        ('Sylhet', 'Sylhet'),
    )
    Area = models.CharField(max_length=50, null=True, choices=area)
    Rating = models.FloatField()
    TotalRating = models.FloatField()
    NumRating = models.IntegerField()

class record(models.Model):
    ruser = models.CharField(max_length=100)
    rdate = models.DateField(auto_now_add=True)
    Test_Name = models.CharField(max_length=100, null=True)
    tlevel = models.FloatField()
    treference = models.CharField(max_length=100, null=True)
    rcomment = models.CharField(max_length=200, null=True)