# Generated by Django 3.1.2 on 2020-12-11 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SARZS', '0033_record_tdoctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='rdate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
