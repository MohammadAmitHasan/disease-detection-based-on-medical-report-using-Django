# Generated by Django 3.1.3 on 2020-11-18 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SARZS', '0016_auto_20201118_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='tname',
            new_name='Test_Name',
        ),
    ]
