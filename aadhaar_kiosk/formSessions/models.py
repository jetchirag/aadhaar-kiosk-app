import uuid
from django.db import models

# Create your models here.
class enrolForm(models.Model):
    uuid = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False,
         max_length=36)


    # Step 1 form fields:
    fullname = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
    ))
    dob = models.DateField()

    # Step 2: Adress
    address_co = models.CharField(max_length=255,null=True)
    address_no = models.CharField(max_length=255,null=True)
    address_2 = models.CharField(max_length=1024,null=True)
    address_landmark = models.CharField(max_length=1024,null=True)
    address_area = models.CharField(max_length=1024,null=True)
    address_city = models.CharField(max_length=255,null=True)
    address_postoffice = models.CharField(max_length=255,null=True)
    address_district = models.CharField(max_length=255,null=True)
    address_subdistrict = models.CharField(max_length=255,null=True)

    # Step 3: Electronic Details
    email = models.EmailField(null=True)
    phone = models.PositiveBigIntegerField(null=True)

    # Step 4: Details of someone else
    details_else_of = models.CharField(max_length=255, choices=(
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Guardian', 'Guardian'),
        ('Husband', 'Husband'),
        ('Wife', 'Wife'),
    ),null=True)
    details_else_name = models.CharField(max_length=255,null=True)
    details_else_no = models.CharField(max_length=255,null=True)

    # Step 5: Verification
    verify_type = models.CharField(max_length=255, choices=(
        ('Document Based', 'Document Based'),
        ('Introducer Based', 'Introducer Based'),
        ('Head of Family (HoF) Based', 'Head of Family (HoF) Based'),
    ),null=True)
    # TODO: Add choices for verification type

    #TODO: Add declaration and final confirmation check

    def __str__(self):
         return str(self.uuid)

        
