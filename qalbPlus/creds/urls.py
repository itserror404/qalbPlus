from django.urls import path
from. import views

#This url pattern sends to the client the views.upload function.
urlpatterns= [
    path('',views.upload,name='upload'),
    #path('', views.home, name= 'home'),

]
