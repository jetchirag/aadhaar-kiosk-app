# Generated by Django 3.2.15 on 2022-08-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formSessions', '0008_rename_fullname_enrolform_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolform',
            name='lastname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='enrolform',
            name='middlename',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
