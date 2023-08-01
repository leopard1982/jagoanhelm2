from django.contrib import admin
from django.urls import path
from penjualan.views import dashboard, logoutUser, detail_produk, dashboard, troli, troli_delete, checkout_awal
from penjualan.views import troli_tambah_kurang, checkout_oke
from penjualan.view_serializers import api_get_produk

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('logout/', logoutUser, name="logoutUser"),
    path('d/', detail_produk, name="detail_produk"),
    path('t/', troli, name='troli'),
    path('t/d/', troli_delete, name="troli_delete"),
    path('t/tk/', troli_tambah_kurang, name="troli_tambah_kurang"),
    path('c/', checkout_awal, name="checkout_awal"),
    path('c/ok/', checkout_oke, name="checkout_oke"),
    path('api/get/produk/', api_get_produk, name="api_get_produk"),

]
