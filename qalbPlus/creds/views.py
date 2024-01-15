from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . forms import CredentialForm
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import redirect
# Create your views here.

def upload(request):
    #return render(request,'creds/home.html')
    #return HttpResponse('<h1>Creds Home </h1>')
    if request.method == 'POST':
        form = CredentialForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view-Appointmentstp')
    else:
        form = CredentialForm()
    return render(request,'main/credForms.html',{'form':form})



def home(request):
	return render(request, "main/home.html", {})
