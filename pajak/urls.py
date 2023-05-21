from django.contrib import admin
from django.urls import path
from pajak.views import dashboard

urlpatterns = [
    path('', dashboard,name="dashboard"),
]
