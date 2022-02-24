from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contributors/', views.contributors), 
    path('form/', views.form),  
    path('test/', views.test), 
]