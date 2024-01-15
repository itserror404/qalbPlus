from django.db import models

class Tptest(models.Model):
    email = models.TextField()
    name = models.TextField()
    address = models.TextField()
    specialty= models.TextField()
    insurance = models.TextField()
    distance = models.FloatField()

class Tptestnew(models.Model):
    email = models.TextField()
    password = models.TextField()
    name = models.TextField()
    address = models.TextField()
    specialty = models.TextField()
    insurance = models.TextField()
    available_times1 = models.TextField()
    available_times2 = models.TextField()
    available_times3 = models.TextField()
    available_times4 = models.TextField()
    available_times5 = models.TextField()
    is_verified = models.BooleanField()
    distance = models.FloatField()
    class Meta:
        app_label = 'armss'

    def __str__(self):
        return self.email

class Appointment(models.Model):
    tpemail = models.TextField()
    tpname = models.TextField()
    patientemail = models.TextField()
    patientname = models.TextField()
    time = models.TextField()
    day = models.TextField()

    class Meta:
        app_label = 'armss'

    def __str__(self):
        return self.tpemail+self.patientemail+self.time+self.day

class CurrentUser(models.Model):
    email = models.TextField()
    name = models.TextField()

    class Meta:
        app_label = 'armss'

    def __str__(self):
        return self.email



