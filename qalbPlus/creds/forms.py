from django.forms import ModelForm
from .models import Credential

class CredentialForm(ModelForm):
    class Meta:
        model = Credential
        fields=['first_name','last_name','email','upload']
