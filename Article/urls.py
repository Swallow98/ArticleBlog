from django.urls import path
from .views import *



urlpatterns = [
    path('Add_Type/',Add_Type),
    path('Select_Type/',Select_Type),
]