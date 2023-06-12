from django.shortcuts import render, HttpResponseRedirect
from administrasi.models import Produk, bannerToko, kategoriProduk

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.core.paginator import Paginator


# Create your views here.
def dashboard(request):
	filter_search=request.GET.get("q")
	if(filter_search==None):
		filter_search=""

	page_search=None
	if request.method=="POST":
		try:
			#apakah post untuk login?
			username=request.POST['txtUsername']
			password=request.POST['txtPassword']
			user=authenticate(username=username,password=password)
			if user != None:
				login(request,user)
				messages.success(request,"Login Berhasil! welcome %s"%username)
			else:
				messages.success(request,"Login Gagal! Username atau password tidak sesuai!")
			return HttpResponseRedirect("/")
		except:
			pass


	tampilkan=True
	filterby=request.GET.get('kat')
	
	mydata = Produk.objects.all().filter(aktif=True)
	
	if filterby != None:
		tampilkan=False
		if(len(filterby)==0):
			filterby="Semua"
		else:
			mydata = mydata.filter(kategori__icontains=filterby)
	
	bannernya = bannerToko.objects.all()
	mykategori = kategoriProduk.objects.all()


	produknya = Produk.objects.all().filter(aktif=True)
	
	if filterby!=None:
		if filterby!="Semua":
			produknya=produknya.filter(kategori__icontains=filterby)
	
	if filter_search!="":
		produknya = produknya.filter(produk_nama__icontains=filter_search)
		messages.success(request,"Pencarian dengan kata kunci: '%s' menghasilkan hasil %i produk!"%(filter_search,produknya.count()))
	
	p = Paginator(produknya,12)

	page_search = request.GET.get('p')

	if isinstance(page_search,int):
		if not page_search>0 and page_search<=p.num_page:
			page_search=1
	p_isi = p.get_page(page_search)	

	jumlah_data = produknya.count()

	return render(request,'penjualan/dashboard.html',{'jumlah_data':jumlah_data,'mykategori':mykategori,'mydata':mydata,'bannernya':bannernya,'tampilkan':tampilkan,'filterby':filterby,'produknya':p_isi})


def logoutUser(request):
	logout(request)
	messages.success(request,"You Are Logout Now!")
	return HttpResponseRedirect("/")