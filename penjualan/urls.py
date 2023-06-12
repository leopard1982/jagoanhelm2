from django.contrib import admin
from django.urls import path
from penjualan.views import dashboard, logoutUser

urlpatterns = [
    path('', dashboard,name="dashboard"),
    path('logout/',logoutUser,name="logoutUser")
]
