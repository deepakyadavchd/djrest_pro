

from django.contrib import admin
from django.urls import path
from .views import*


urlpatterns = [
    path('helloworld/', helloview),
    path('insert/', insertview),
    path('cars/', carsview), 
    path('filter/', filterview),
    path('delete/', deleteview)


]




