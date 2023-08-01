from rest_framework.response import Response
from administrasi.models import masterDesa, masterKota, masterProvinsi
from administrasi.serialezersnya import serializerDesa, serializerKota, serializerProvinsi
from rest_framework.decorators import api_view


@api_view(['POST', 'GET'])
def api_master_desa(request):
    myserial = None
    if request.method == 'POST':
        print(request.data)
        if "prov" and "kota" in request.data.keys():
            mydata = masterDesa.objects.all().filter(
                kode_provinsi=masterProvinsi.objects.get(
                    nama_provinsi=request.data['prov']),
                kode_kota=masterKota.objects.get(nama_kota=request.data['kota']))
            myserial = serializerDesa(mydata, many=True)
            myserial = myserial.data
    return Response({'result': myserial})


@api_view(['POST', 'GET'])
def api_master_kota(request):
    myserial = None
    if request.method == 'POST':
        if "prov" in request.data.keys():
            mydata = masterKota.objects.all().filter(
                kode_provinsi=masterProvinsi.objects.get(nama_provinsi=request.data["prov"]))
            myserial = serializerKota(mydata, many=True)
            myserial = myserial.data
    return Response({'result': myserial})


@api_view(['POST', 'GET'])
def api_master_provinsi(request):
    myserial = None
    if request.method == 'POST':
        if "prov" in request.data.keys():
            mydata = masterProvinsi.objects.all()
            myserial = serializerProvinsi(mydata, many=True)
            myserial = myserial.data
            print(myserial)
        # mydata = masterProvinsi.objects.all()
        # myserial = serializerProvinsi(mydata)
        # myserial = myserial.data()
    return Response({'result': myserial})
