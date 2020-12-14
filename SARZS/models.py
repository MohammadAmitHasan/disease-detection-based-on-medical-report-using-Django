from django.db import models
from django.contrib.auth.models import User

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
    Rating = models.FloatField(null=True)
    TotalRating = models.FloatField(null=True)
    numberOfRating = models.IntegerField(null=True, default=0)
    photo = models.ImageField(upload_to="images" , null = True)

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
    Rating = models.FloatField(null=True)
    TotalRating = models.FloatField(null=True)
    numberOfRating = models.IntegerField(null=True, default=0)
    photo = models.ImageField(upload_to="images" , null = True)

class doctor_list(models.Model):
    DOCid = models.CharField(max_length=10, null=True)
    Name = models.CharField(max_length=100, null=True)
    Designation = models.CharField(max_length=200, null=True)
    Qualification = models.CharField(max_length=200, null=True)
    Department = models.CharField(max_length=200, null=True)
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
    photo = models.ImageField(upload_to="images", null=True, blank=True)
    rating = models.FloatField(null=True, default=0)
    totalRating = models.FloatField(null=True, default=0)
    numberOfRating = models.IntegerField(null=True, default=0)
    def __str__(self):
        return self.Name

class record(models.Model):
    rid = models.IntegerField(default=1)
    rdate = models.DateTimeField(auto_now_add=True, null=True)
    Test_Name = models.CharField(max_length=100, null=True)
    tlevel = models.FloatField()
    treference = models.CharField(max_length=100, null=True)
    rcomment = models.CharField(max_length=200, null=True)
    tdoctor = models.CharField(max_length=100, null=True)

class docReview(models.Model):
    DOCid = models.CharField(max_length=10, null=True)
    user = models.CharField(max_length=100, null=True)
    comment = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user

class hospitalReview(models.Model):
    Hid = models.CharField(max_length=10, null=True)
    user = models.CharField(max_length=100, null=True)
    comment = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

class diagnosticReview(models.Model):
    Did = models.CharField(max_length=10, null=True)
    user = models.CharField(max_length=100, null=True)
    comment = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
