from django.db import models
from userentry.models import User
# Create your models here.

# Creates a model that the ORM maps to the database fields. The fields are self explanatory.
class Credential(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')
    upload = models.FileField(default='degree',upload_to='user_credentials')





