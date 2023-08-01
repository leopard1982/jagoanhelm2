from administrasi.models import Produk
from rest_framework import serializers


class serializersProduk(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = "__all__"
