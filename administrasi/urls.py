from django.contrib import admin
from django.urls import path
from administrasi.views import dashboard,upload_Produk, upload_Kategori, input_kategoriProduk, input_Produk
from administrasi.views import viewProduk, updateProduk, downTemplateProduk,downTemplateKategori,delete_Produk
from administrasi.views import viewkategoriProduk, delete_Kategori, updateKategori, updateStatusProduk
from administrasi.views import inputStokRusak, viewStatusStokRusak, updateStokRusak, deleterusakProduk
from administrasi.views import InputRevisiStokManual, viewStatusRevisiStok, UpdateRevisiStokManual
from administrasi.views import deleteRevisiProduk, inputBannerToko, deleteBanner, updateBanner

urlpatterns = [
    path('', dashboard,name="dashboard"),
    path('input/banner/',inputBannerToko,name="inputBannerToko"),
    path('input/kategori/',input_kategoriProduk,name="inputKategoriProduk"),
    path('input/produk/',input_Produk,name="inputProduk"),
    path('input/produk/rusak/<str:produk_kode>/',inputStokRusak,name="inputStokRusak"),
    path('input/produk/rev_stok/<str:produk_kode>/',InputRevisiStokManual,name="InputRevisiStokManual"),
    path('upload/produk/',upload_Produk,name="uploadProduk"),
    path('upload/kategori/',upload_Kategori,name="uploadKategori"),
    path('view/produk/',viewProduk,name="viewProduk"),
    path('view/kategoriproduk/',viewkategoriProduk,name="viewkategoriProduk"),
    path('view/produk/rusak/',viewStatusStokRusak,name="viewStatusStokRusak"),
    path('view/produk/revisi/',viewStatusRevisiStok,name="viewStatusRevisiStok"),
    path('download/template/produk/',downTemplateProduk,name="downTemplateProduk"),
    path('download/template/kategori/',downTemplateKategori,name="downTemplateKategori"),
    path('update/<str:produk_kode>/produk/',updateProduk,name="updateProduk"),
    path('update/produk/status/',updateStatusProduk,name="updateStatusProduk"),
    path('update/<str:kategori>/kategori/',updateKategori,name="updateKategori"),
    path('update/produk/rusak/<int:pk>/',updateStokRusak,name="updateStokRusak"),
    path('update/produk/revisi/<int:pk>/',UpdateRevisiStokManual,name="UpdateRevisiStokManual"),
    path('update/banner/<int:pk>/',updateBanner,name="updateBanner"),
    path('delete/<str:produk_kode>/produk/',delete_Produk,name="deleteProduk"),
    path('delete/<str:kategori>/kategori/',delete_Kategori,name="deleteKategori"),
    path('delete/<int:pk>/produk/rusak/',deleterusakProduk,name="deleterusakProduk"),
    path('delete/<int:pk>/produk/revisi/',deleteRevisiProduk,name="deleteRevisiProduk"),
    path('delete/<int:pk>/banner/',deleteBanner,name="deleteBanner"),
]
