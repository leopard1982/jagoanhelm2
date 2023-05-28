from django.contrib import admin
from django.urls import path
from administrasi.views import dashboard,upload_Produk, upload_Kategori, input_kategoriProduk, input_Produk
from administrasi.views import viewProduk, updateProduk, downTemplateProduk,downTemplateKategori,delete_Produk
from administrasi.views import viewkategoriProduk, delete_Kategori, updateKategori

urlpatterns = [
    path('', dashboard,name="dashboard"),
    path('input/kategori/',input_kategoriProduk,name="inputKategoriProduk"),
    path('input/produk/',input_Produk,name="inputProduk"),
    path('upload/produk/',upload_Produk,name="uploadProduk"),
    path('upload/kategori/',upload_Kategori,name="uploadKategori"),
    path('view/produk/',viewProduk,name="viewProduk"),
    path('view/kategoriproduk/',viewkategoriProduk,name="viewkategoriProduk"),
    path('download/template/produk/',downTemplateProduk,name="downTemplateProduk"),
    path('download/template/kategori/',downTemplateKategori,name="downTemplateKategori"),
    path('update/<str:produk_kode>/produk/',updateProduk,name="updateProduk"),
    path('update/<str:kategori>/kategori/',updateKategori,name="updateKategori"),
    path('delete/<str:produk_kode>/produk/',delete_Produk,name="deleteProduk"),
    path('delete/<str:kategori>/kategori/',delete_Kategori,name="deleteKategori"),
]
