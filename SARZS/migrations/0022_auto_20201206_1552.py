# Generated by Django 3.1.2 on 2020-12-06 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SARZS', '0021_auto_20201119_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor_list',
            old_name='tdoctor',
            new_name='Department',
        ),
    ]