from django.contrib import admin
from django.urls import path
from administrasi.views import dashboard,upload_Produk, input_kategoriProduk, input_Produk
from administrasi.views import viewProduk, updateProduk, downTemplateProduk

urlpatterns = [
    path('', dashboard,name="dashboard"),
    path('input/kategori/',input_kategoriProduk,name="inputKategoriProduk"),
    path('input/produk/',input_Produk,name="inputProduk"),
    path('upload/produk/',upload_Produk,name="uploadProduk"),
    path('view/produk/',viewProduk,name="viewProduk"),
    path('download/template/produk',downTemplateProduk,name="downTemplateProduk"),
    path('update/<str:produk_kode>/produk/',updateProduk,name="updateProduk")
]
