# Generated by Django 3.2.15 on 2022-08-25 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formSessions', '0007_auto_20220825_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrolform',
            old_name='fullname',
            new_name='firstname',
        ),
    ]
