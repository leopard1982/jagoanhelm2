from django.contrib import admin
from django.urls import path
from administrasi.views import dashboard, upload_Produk, upload_Kategori, input_kategoriProduk, input_Produk
from administrasi.views import viewProduk, updateProduk, downTemplateProduk, downTemplateKategori, delete_Produk
from administrasi.views import viewkategoriProduk, delete_Kategori, updateKategori, updateStatusProduk
from administrasi.views import inputStokRusak, viewStatusStokRusak, updateStokRusak, deleterusakProduk
from administrasi.views import InputRevisiStokManual, viewStatusRevisiStok, UpdateRevisiStokManual
from administrasi.views import deleteRevisiProduk, inputBannerToko, deleteBanner, updateBanner, logoutNow
from administrasi.views import sinkronData, masterProvinsi_view, masterProvinsi_delete, masterProvinsi_upload
from administrasi.views import masterKota_view, masterKota_delete, masterKota_upload, masterDesa_view
from administrasi.views import masterDesa_delete, masterDesa_upload
from administrasi.views_api import api_master_desa, api_master_kota, api_master_provinsi

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('sinkron/', sinkronData, name="sinkronData"),
    path('logout/', logoutNow, name="logoutNow"),
    path('input/banner/', inputBannerToko, name="inputBannerToko"),
    path('input/kategori/', input_kategoriProduk, name="inputKategoriProduk"),
    path('input/produk/', input_Produk, name="inputProduk"),
    path('input/produk/rusak/<str:produk_kode>/',
         inputStokRusak, name="inputStokRusak"),
    path('input/produk/rev_stok/<str:produk_kode>/',
         InputRevisiStokManual, name="InputRevisiStokManual"),
    path('upload/produk/', upload_Produk, name="uploadProduk"),
    path('upload/kategori/', upload_Kategori, name="uploadKategori"),
    path('view/produk/', viewProduk, name="viewProduk"),
    path('view/kategoriproduk/', viewkategoriProduk, name="viewkategoriProduk"),
    path('view/produk/rusak/', viewStatusStokRusak, name="viewStatusStokRusak"),
    path('view/produk/revisi/', viewStatusRevisiStok,
         name="viewStatusRevisiStok"),
    path('download/template/produk/',
         downTemplateProduk, name="downTemplateProduk"),
    path('download/template/kategori/',
         downTemplateKategori, name="downTemplateKategori"),
    path('update/<str:produk_kode>/produk/',
         updateProduk, name="updateProduk"),
    path('update/produk/status/', updateStatusProduk, name="updateStatusProduk"),
    path('update/<str:kategori>/kategori/',
         updateKategori, name="updateKategori"),
    path('update/produk/rusak/<int:pk>/',
         updateStokRusak, name="updateStokRusak"),
    path('update/produk/revisi/<int:pk>/',
         UpdateRevisiStokManual, name="UpdateRevisiStokManual"),
    path('update/banner/<int:pk>/', updateBanner, name="updateBanner"),
    path('delete/<str:produk_kode>/produk/',
         delete_Produk, name="deleteProduk"),
    path('delete/<str:kategori>/kategori/',
         delete_Kategori, name="deleteKategori"),
    path('delete/<int:pk>/produk/rusak/',
         deleterusakProduk, name="deleterusakProduk"),
    path('delete/<int:pk>/produk/revisi/',
         deleteRevisiProduk, name="deleteRevisiProduk"),
    path('delete/<int:pk>/banner/', deleteBanner, name="deleteBanner"),
    # masterdata
    path('master/prov/', masterProvinsi_view, name="masterProvinsi_view"),
    path('master/prov/d/', masterProvinsi_delete, name="masterProvinsi_delete"),
    path('master/prov/u/', masterProvinsi_upload, name="masterProvinsi_upload"),
    path('api/master/provinsi/', api_master_provinsi, name="api_master_provinsi"),
    path('master/kota/', masterKota_view, name="masterKota_view"),
    path('master/kota/d/', masterKota_delete, name="masterKota_delete"),
    path('master/kota/u/', masterKota_upload, name="masterKota_upload"),
    path('api/master/kota/', api_master_kota, name="api_master_kota"),
    path('master/desa/', masterDesa_view, name="masterDesa_view"),
    path('master/desa/d/', masterDesa_delete, name="masterDesa_delete"),
    path('master/desa/u/', masterDesa_upload, name="masterDesa_upload"),
    path('api/master/desa/', api_master_desa, name="api_master_desa")
]
