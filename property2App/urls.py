from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contributors/', views.contributors), 
    path('form/', views.form),  
    path('test/', views.test), 
    path('add-new/', views.newMembers),
    path ('results/', views.results),
    path ('the-shop/', views.theShop),
    path('reset/', views.reset),
    path('purchase/', views.purchase),
    path('skills/', views.skills),
    path('neighbor/', views.neighbor),
    path('addNew/', views.addNeighbor),
    path('create/', views.create),
]