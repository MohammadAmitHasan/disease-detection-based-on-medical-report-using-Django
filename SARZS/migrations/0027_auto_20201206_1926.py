# Generated by Django 3.1.2 on 2020-12-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SARZS', '0026_doctor_list_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosticcomment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='doccomment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='hospitalcomment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]