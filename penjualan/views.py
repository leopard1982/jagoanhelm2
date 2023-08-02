from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from administrasi.models import Produk, bannerToko, kategoriProduk

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.core.paginator import Paginator

from django.db.models import F, Q

from django.core.mail import send_mail, EmailMultiAlternatives

from django.template.loader import render_to_string

from django.conf import settings


# Create your views here.
def dashboard(request):
    # HttpResponse.set_cookie(key="test", value="hallo")
    filter_search = request.GET.get("q")
    if (filter_search == None):
        filter_search = ""

    page_search = None
    if request.method == "POST":
        try:
            # apakah post untuk login?
            username = request.POST['txtUsername']
            password = request.POST['txtPassword']
            user = authenticate(username=username, password=password)
            if user != None:
                login(request, user)
                messages.success(
                    request, "Login Berhasil! welcome %s" % username)
            else:
                messages.success(
                    request, "Login Gagal! Username atau password tidak sesuai!")
            return HttpResponseRedirect("/")
        except:
            pass

    tampilkan = True
    filterby = request.GET.get('kat')

    mydata = Produk.objects.all().filter(aktif=True)

    if filterby != None:
        tampilkan = False
        if (len(filterby) == 0):
            filterby = "Semua"
        else:
            mydata = mydata.filter(kategori__icontains=filterby)

    bannernya = bannerToko.objects.all()
    mykategori = kategoriProduk.objects.all()

    produknya = Produk.objects.all().filter(aktif=True)

    if filterby != None:
        if filterby != "Semua":
            produknya = produknya.filter(kategori__icontains=filterby)

    if filter_search != "":
        produknya = produknya.filter(produk_nama__icontains=filter_search)
        messages.success(request, "Pencarian dengan kata kunci: '%s' menghasilkan hasil %i produk!" % (
            filter_search, produknya.count()))

    p = Paginator(produknya, 12)

    page_search = request.GET.get('p')

    if isinstance(page_search, int):
        if not page_search > 0 and page_search <= p.num_page:
            page_search = 1
    p_isi = p.get_page(page_search)

    jumlah_data = produknya.count()

    request.session['wishlist'] = []
    request.session['wishlist'] += [{
        'id': 'abc',
    }]
    request.session['wishlist'] += [{
        'id': 'def',
    }]
    try:
        shopping_chart_jml = len(request.session['cart'])
    except:
        shopping_chart_jml = 0
        request.session['cart'] = []
    wishlish = len(request.session['wishlist'])

    sc = request.session['cart']

    contex = {
        'shopping_chart_jml': shopping_chart_jml,
        'wishlist': wishlish,
        'sc': sc,
        'jumlah_data': jumlah_data,
        'mykategori': mykategori,
        'mydata': mydata,
        'bannernya': bannernya,
        'tampilkan': tampilkan,
        'filterby': filterby,
        'produknya': p_isi
    }

    return render(request, 'penjualan/dashboard.html', contex)


def logoutUser(request):
    logout(request)
    messages.success(request, "You Are Logout Now!")
    return HttpResponseRedirect("/")


def detail_produk(request):
    produknya = request.GET.get('pid')
    if produknya is not None:
        try:
            detail_datanya = Produk.objects.get(produk_kode=produknya)
        except:
            return HttpResponseRedirect("/")

        Produk.objects.all().filter(disc_active=True).update(
            harga_nett=F("harga")-F("disc"))
        produk = Produk.objects.all().filter(~Q(kategori=detail_datanya.kategori))

        # request.session['cart'] = []
        # request.session['cart'] += [{
        #     'produk_kode': 'abc',
        #     'nama': 'Helm Merek Sindoro',
        #     'jumlah': 2}]
        # request.session['cart'] += [{
        #     'id': 'def',
        #     'nama': 'Helm Merek Sumbing',
        #     'jumlah': 3}]
        request.session['wishlist'] = []
        request.session['wishlist'] += [{
            'id': 'abc',
        }]
        request.session['wishlist'] += [{
            'id': 'def',
        }]
        try:
            shopping_chart_jml = len(request.session['cart'])
        except:
            shopping_chart_jml = 0
            request.session['cart'] = []
        wishlish = len(request.session['wishlist'])

        sc = request.session['cart']

        jumlah = 0
        if (len(sc) == 0):
            jumlah = 0
        else:
            for mycart in sc:
                if mycart['produk_kode'] == produknya:
                    jumlah = mycart['jumlah']
                    break

        contex = {
            'shopping_chart_jml': shopping_chart_jml,
            'wishlist': wishlish,
            'sc': sc,
            'produk': produk,
            'detail_datanya': detail_datanya,
            'jumlah_awal': jumlah
        }
        return render(request, "penjualan/buy.html", contex)
    else:
        return HttpResponseRedirect("/")


def troli(request):
    if request.method == "POST":
        i = 0
        mycart = request.session['cart']
        sudah_ditambahkan = False

        for cart in mycart:
            if cart['produk_kode'] == request.POST['kode_produk']:
                mycart[i]['jumlah'] = int(
                    mycart[i]['jumlah']) + int(request.POST['jumlah'])
                sudah_ditambahkan = True
                mycart[i]['gambar'] = request.POST['gambar']
                request.session['cart'] = mycart
                break
            i += 1

        if sudah_ditambahkan == False:
            request.session['cart'] += [
                {
                    'produk_kode': request.POST['kode_produk'],
                    'produk_nama': request.POST['nama_produk'],
                    'jumlah':request.POST['jumlah'],
                    'gambar':request.POST['gambar'],
                }
            ]
        print(request.session['cart'])
        print(len(request.session['cart']))

        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


def troli_delete(request):
    cartnya = request.session['cart']
    if request.method == 'POST':
        produk_kode = request.POST['produk_kode']
        i = 0
        for cartku in cartnya:
            if cartku['produk_kode'] == produk_kode:
                print('ketemu')
                del cartnya[i]
                break
            i += 1

    request.session['cart'] = cartnya

    return HttpResponseRedirect('/')


def troli_tambah_kurang(request):
    cartnya = request.session['cart']
    if request.method == 'POST':
        produk_kode = request.POST['produk_kode']
        tambah_kurang = request.POST['tambah_kurang']
        print(produk_kode)
        print(tambah_kurang)
        i = 0
        for cartku in cartnya:
            if cartku['produk_kode'] == produk_kode:
                if tambah_kurang == "tambah":
                    cartnya[i]['jumlah'] = int(cartku['jumlah'])+1
                    # print(cartnya[i])
                    request.session['cartnya'] = cartnya
                    break
                if tambah_kurang == "kurang":
                    jml = int(cartku['jumlah'])-1
                    if (jml == 0):
                        del cartnya[i]
                    else:
                        cartnya[i]['jumlah'] = jml
                    # print(cartnya[i])
                    request.session['cartnya'] = cartnya
                    break
            i += 1
    return HttpResponseRedirect("/")


def checkout_awal(request):
    nama_item = None
    if request.GET.get("item") != "":
        nama_item = request.GET.get("item")

    request.session['wishlist'] = []
    request.session['wishlist'] += [{
        'id': 'abc',
    }]
    request.session['wishlist'] += [{
        'id': 'def',
    }]
    try:
        shopping_chart_jml = len(request.session['cart'])
    except:
        shopping_chart_jml = 0
        return HttpResponseRedirect('/')

    wishlish = len(request.session['wishlist'])

    sc = request.session['cart']

    contex = {
        'shopping_chart_jml': shopping_chart_jml,
        'wishlist': wishlish,
        'sc': sc,
        'item': nama_item
    }
    return render(request, "penjualan/checkout.html", contex)


def checkout_oke(request):
    if request.method == "POST":
        konteks = {
            'nama': request.POST['namanya'],
            'pembayaran': request.POST['total_belanja'],
            'no_wa': request.POST['no_wa'],
        }
        content_text = render_to_string(
            'email/konfirmasiBuy.txt', konteks, request=request)
        content_html = render_to_string(
            'email/konfirmasiBuy.html', konteks, request=request)
        emailSubject = "jagoanhelm.com - konfirmasi pembelian #" + \
            request.POST['namanya']
        emailSender = settings.EMAIL_HOST_USER
        emailRecipient = request.POST['emailnya']

        # I used EmailMultiAlternatives because I wanted to send both text and html
        emailMessage = EmailMultiAlternatives(subject=emailSubject, body=content_text, from_email=emailSender, to=[
                                              emailRecipient], reply_to=[emailSender,])
        emailMessage.attach_alternative(content_html, "text/html")
        emailMessage.send(fail_silently=False)

    return HttpResponseRedirect("/")
