# Generated by Django 3.1.2 on 2020-11-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SARZS', '0012_auto_20201108_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitals',
            name='hdivision',
            field=models.CharField(choices=[('Barishal', 'Barishal '), ('Chittagong', 'Chittagong '), ('Dhaka', 'Dhaka'), ('Mymensingh', 'Mymensingh'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet')], max_length=200, null=True),
        ),
    ]
