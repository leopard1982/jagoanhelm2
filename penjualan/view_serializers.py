from administrasi.models import Produk
from penjualan.myserializers import serializersProduk
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q


@api_view(['GET', 'POST'])
def api_get_produk(request):
    if request.method == 'POST':
        # try:
        #     datanya = dict(request.data)
        #     filternya = datanya['datanya[]']
        #     qfilter = "Q(produk_kode='%s')" % filternya[0]
        #     i = 0
        #     for filter in filternya:
        #         if (i > 0):
        #             qfilter = qfilter + " | " + "Q(produk_kode='%s')" % filter
        #         i += 1
        #     # print(qfilter)
        #     filter = qfilter  # gotcha!!!!
        # except:
        #     pass
        datanya = dict(request.data)
        print(datanya)
        filternya = []
        try:
            filternya = datanya['datanya[]']
        except:
            filternya = []
        print(len(filternya))

        produk = Produk.objects.all()
        mydata = []
        for prod in produk:
            if (prod.produk_kode == "ABCD413"):
                print(prod.produk_kode + prod.produk_nama +
                      " - " + str(prod.harga))
            for filter in filternya:
                if (prod.produk_kode == filter):
                    diskon = 0
                    if prod.disc_active:
                        diskon = prod.disc
                    try:
                        x = {
                            'produk_kode': prod.produk_kode,
                            'produk_nama': prod.produk_nama,
                            'harga': prod.harga,
                            'gambar': prod.gambar.url,
                            'diskon': diskon,
                        }
                    except:
                        x = {
                            'produk_kode': prod.produk_kode,
                            'produk_nama': prod.produk_nama,
                            'harga': prod.harga,
                            'gambar': "",
                            'diskon': diskon,
                        }
                    mydata.append(x)
                    break
        # URUTKAN DAN KEMBALIKAN MENURUT URUTAN DATA AWAL
        mydata_send = []
        for filter in filternya:
            for data in mydata:
                if (data['produk_kode'] == filter):
                    mydata_send.append(data)

        print(mydata_send)
        return Response(mydata_send)

    myproduk = Produk.objects.all()

    mydata = []

    # if (filter == ""):
    #     myproduk = Produk.objects.all()
    # else:
    #     myproduk = Produk.objects.all().filter(filter)

    serialnya = serializersProduk(myproduk, many=True)
    return Response(serialnya.data)
