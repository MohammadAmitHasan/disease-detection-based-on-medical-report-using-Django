# Generated by Django 3.1.2 on 2020-12-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SARZS', '0034_auto_20201211_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='ruser',
        ),
        migrations.AddField(
            model_name='record',
            name='rid',
            field=models.IntegerField(default=1),
        ),
    ]
