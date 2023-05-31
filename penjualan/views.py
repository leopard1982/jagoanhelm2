from django.shortcuts import render
from administrasi.models import Produk

# Create your views here.
def dashboard(request):
	mydata = Produk.objects.all().filter(aktif=True)

	return render(request,'penjualan/dashboard.html',{'mydata':mydata})