from django.shortcuts import render
from administrasi.models import Produk, bannerToko, kategoriProduk

# Create your views here.
def dashboard(request):
	tampilkan=True
	filterby=request.GET.get('kat')
	
	mydata = Produk.objects.all().filter(aktif=True)
	
	if filterby != None:
		tampilkan=False
		if(len(filterby)==0):
			filterby="Semua"
		else:
			mydata = mydata.filter(kategori_id=filterby)
	
	jumlah_data = mydata.count()

	bannernya = bannerToko.objects.all()
	mykategori = kategoriProduk.objects.all()
	return render(request,'penjualan/dashboard.html',{'jumlah_data':jumlah_data,'mykategori':mykategori,'mydata':mydata,'bannernya':bannernya,'tampilkan':tampilkan,'filterby':filterby})