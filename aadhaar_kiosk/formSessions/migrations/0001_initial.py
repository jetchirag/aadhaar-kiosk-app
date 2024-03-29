# Generated by Django 3.2.15 on 2022-08-18 03:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='enrolForm',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], max_length=1)),
                ('dob', models.DateField()),
                ('address_co', models.CharField(max_length=255, null=True)),
                ('address_no', models.CharField(max_length=255, null=True)),
                ('address_2', models.CharField(max_length=1024, null=True)),
                ('address_landmark', models.CharField(max_length=1024, null=True)),
                ('address_area', models.CharField(max_length=1024, null=True)),
                ('address_city', models.CharField(max_length=255, null=True)),
                ('address_postoffice', models.CharField(max_length=255, null=True)),
                ('address_district', models.CharField(max_length=255, null=True)),
                ('address_subdistrict', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.PositiveBigIntegerField(null=True)),
                ('details_else_of', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Guardian', 'Guardian'), ('Husband', 'Husband'), ('Wife', 'Wife')], max_length=255, null=True)),
                ('details_else_name', models.CharField(max_length=255, null=True)),
                ('details_else_no', models.CharField(max_length=255, null=True)),
                ('verify_type', models.CharField(choices=[('Document Based', 'Document Based'), ('Introducer Based', 'Introducer Based'), ('Head of Family (HoF) Based', 'Head of Family (HoF) Based')], max_length=255, null=True)),
            ],
        ),
    ]
