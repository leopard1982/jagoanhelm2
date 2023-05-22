from django.contrib import admin
from django.urls import path
from administrasi.views import dashboard, input_kategoriProduk, input_Produk

urlpatterns = [
    path('', dashboard,name="dashboard"),
    path('input/kategori/',input_kategoriProduk,name="inputKategoriProduk"),
    path('input/produk/',input_Produk,name="inputProduk"),
]
