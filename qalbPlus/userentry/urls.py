#this file tracks or maintains the various urls created in the application.

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path("login/", views.log_in, name='log_in'),
    path("registeruser/", views.registeruser, name="registeruser"),
    path("registerTP/", views.registerTP, name="registerTP"),
    path("registerPatient/", views.registerPatient, name="registerPatient"),
    path("patient/", views.patient, name='patient'),
    path("tp/", views.tp, name="tp")

]