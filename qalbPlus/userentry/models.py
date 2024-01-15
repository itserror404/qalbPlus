from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.

class Meta:
    app_label  = 'userentry'

STARTTIME= [
    ('9:00', '9:00'),
    ('9:30', '9:30'),
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ]

ENDTIME= [
    ('9:00', '9:00'),
    ('9:30', '9:30'),
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
]

INSURANCE=[
    ('OIC','OIC'),
    ('GEOBLUE', 'GEOBLUE'),
    ('ADNIC', 'ADNIC')
    ]

SPECIALTY=[('GP','GP'),
            ('Dentist', 'Dentist'),
            ('opt', 'Ophthalmologist'),
            ('ENT','ENT')]

#user model stores all data related to users (TP and Patient)
class User(AbstractUser):
    #----main two user----
    is_admin=models.BooleanField("Admin: ",default=False)
    is_tp=models.BooleanField("TP: ",default=False)
    is_patient=models.BooleanField("Patient: ",default=False)

    #unique field to make sure same email is not used
    email = models.CharField(default='', max_length=1000, unique=True)

    password = models.CharField(default='', max_length=1000)
    name = models.CharField(default='', max_length=1000)
    address = models.CharField(default='', max_length=1000)
    age= models.CharField(default='', max_length=1000)

    starttime=models.CharField(
        max_length=5,
        choices=STARTTIME,
        default='',
        blank=True
    )
    endtime = models.CharField(
        max_length=5,
        choices=ENDTIME,
        default='',
        blank=True
    )

    specialty = models.CharField(
        max_length=100,
        choices=SPECIALTY,
        default='',
        blank=True
    )


    insuranceaccepted = models.CharField(
        max_length=100,
        choices=INSURANCE,
        default='',
        blank=True
    )

    insurancedetails = models.CharField(
        max_length=100,
        choices=INSURANCE,
        default='',
        blank=True
    )

    available_times1 = models.CharField(default='',blank=True, max_length=1000)
    available_times2 = models.CharField(default='', blank=True, max_length=1000)
    available_times3 = models.CharField(default='', blank=True, max_length=1000)
    available_times4 = models.CharField(default='', blank=True, max_length=1000)
    available_times5 = models.CharField(default='', blank=True,max_length=1000)

    is_verified = models.BooleanField(default=False, blank=True) #field to check if TP is verified
    distance = models.FloatField(default=0, blank=True)


