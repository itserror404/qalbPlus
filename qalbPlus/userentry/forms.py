from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class Loginf(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput()) #hides the text of the password

class Signupf(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()  # field for password confirmation

    #this class calls an instance of the model including its fields.
    class Meta:
        model = User
        fields = ('insurancedetails', 'username', 'email', 'password1', 'password2', 'is_tp', 'is_admin', 'is_patient', 'name', 'address', 'specialty', 'insuranceaccepted', 'insurancedetails',
                  'is_verified', 'distance', 'available_times1','available_times2','available_times3','available_times4','available_times5', 'starttime', 'endtime', 'age')
