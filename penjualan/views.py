from django.shortcuts import render
from administrasi.models import Produk, bannerToko, kategoriProduk

# Create your views here.
def dashboard(request):
	tampilkan=True
	filterby=request.GET.get('kat')
	
	if filterby != None:
		tampilkan=False
		if(len(filterby)==0):
			filterby="Tampilkan Semua Kategori"
	
	mydata = Produk.objects.all().filter(aktif=True)
	bannernya = bannerToko.objects.all()
	mykategori = kategoriProduk.objects.all()
	return render(request,'penjualan/dashboard.html',{'mykategori':mykategori,'mydata':mydata,'bannernya':bannernya,'tampilkan':tampilkan,'filterby':filterby})