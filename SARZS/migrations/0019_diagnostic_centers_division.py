# Generated by Django 3.1.2 on 2020-11-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SARZS', '0018_auto_20201118_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostic_centers',
            name='Division',
            field=models.CharField(choices=[('Barishal', 'Barishal '), ('Chittagong', 'Chittagong '), ('Dhaka', 'Dhaka'), ('Mymensingh', 'Mymensingh'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet')], max_length=50, null=True),
        ),
    ]
