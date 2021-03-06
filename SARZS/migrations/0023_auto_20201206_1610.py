# Generated by Django 3.1.2 on 2020-12-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SARZS', '0022_auto_20201206_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='diagnosticComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Did', models.CharField(max_length=10, null=True)),
                ('Name', models.CharField(max_length=100, null=True)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='docComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOCid', models.CharField(max_length=10, null=True)),
                ('Name', models.CharField(max_length=100, null=True)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hospitalComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hid', models.CharField(max_length=10, null=True)),
                ('Name', models.CharField(max_length=100, null=True)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='diagnostic_centers',
            name='NumRating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='diagnostic_centers',
            name='Rating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='diagnostic_centers',
            name='TotalRating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='hospitals',
            name='NumRating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hospitals',
            name='Rating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='hospitals',
            name='TotalRating',
            field=models.FloatField(null=True),
        ),
    ]
