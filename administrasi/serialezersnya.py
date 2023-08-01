from rest_framework import serializers
from administrasi.models import masterDesa, masterKota, masterProvinsi


class serializerProvinsi(serializers.ModelSerializer):
    class Meta:
        model = masterProvinsi
        fields = "__all__"


class serializerKota(serializers.ModelSerializer):
    class Meta:
        model = masterKota
        fields = "__all__"


class serializerDesa(serializers.ModelSerializer):
    class Meta:
        model = masterDesa
        fields = "__all__"
