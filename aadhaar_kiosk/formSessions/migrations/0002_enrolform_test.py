# Generated by Django 3.2.15 on 2022-08-18 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formSessions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolform',
            name='test',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
