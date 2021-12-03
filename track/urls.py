from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IPInformation, name='IPInfomation'),
    path('api', views.IPInformationAPI, name='IPInfomation API'),    
]
