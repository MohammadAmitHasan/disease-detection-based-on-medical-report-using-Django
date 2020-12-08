# Generated by Django 3.1.2 on 2020-12-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SARZS', '0029_doctor_list_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docreview',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='docreview',
            name='rating',
        ),
        migrations.AddField(
            model_name='docreview',
            name='DOCid',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='doctor_list',
            name='numberOfRating',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='doctor_list',
            name='totalRating',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='docreview',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_list',
            name='rating',
            field=models.FloatField(default=0, null=True),
        ),
    ]