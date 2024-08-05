from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'), #if anyone comes up with a blank path then send it to index function of views and name the path home.
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name='contact'),
    path("services/",views.services,name='services'),
]