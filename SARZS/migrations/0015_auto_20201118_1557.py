# Generated by Django 3.1.2 on 2020-11-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SARZS', '0014_auto_20201118_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitals',
            name='Division',
            field=models.CharField(choices=[('Barishal', 'Barishal '), ('Chittagong', 'Chittagong '), ('Dhaka', 'Dhaka'), ('Mymensingh', 'Mymensingh'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='Type',
            field=models.CharField(choices=[('Government', 'Government'), ('Private', 'Private')], max_length=50, null=True),
        ),
    ]
