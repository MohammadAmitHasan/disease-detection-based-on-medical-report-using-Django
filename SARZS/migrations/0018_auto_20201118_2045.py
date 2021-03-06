# Generated by Django 3.1.2 on 2020-11-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SARZS', '0017_auto_20201118_2012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagnostic_centers',
            old_name='daddress',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='diagnostic_centers',
            old_name='dcontact',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='diagnostic_centers',
            old_name='did',
            new_name='Did',
        ),
        migrations.RenameField(
            model_name='diagnostic_centers',
            old_name='dname',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='diagnostic_centers',
            old_name='dweb',
            new_name='Website',
        ),
        migrations.RemoveField(
            model_name='diagnostic_centers',
            name='dtype',
        ),
        migrations.AddField(
            model_name='diagnostic_centers',
            name='Type',
            field=models.CharField(choices=[('Government', 'Government'), ('Private', 'Private')], max_length=50, null=True),
        ),
    ]
