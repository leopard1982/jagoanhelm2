from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

from django.db import transaction

from administrasi.forms import formInputKategori, formInputProduk

from administrasi.reads import readdata

# Create your views here.
def dashboard(request):
	return render(request,'administrasi/dashboard.html')

def input_kategoriProduk(request):
	# read data from files
	# try to upload csv (comma separated)
	# readdata.insertToTable()

	if request.method == "POST":
		myform=formInputKategori(request.POST, request.FILES)
		if myform.is_valid():
			myform.save()
		print(myform)
		return HttpResponseRedirect("/adm/input/kategori/")
		
	forms=formInputKategori()
	return render(request,'administrasi/inputKategoriProduk.html',{'forms':forms})

def input_Produk(request):
	if request.method=="POST":
		myform = formInputProduk(request.POST, request.FILES)
		if myform.is_valid():
			myform.save()
		print(myform)
		return HttpResponseRedirect("/adm/input/produk/")	
	forms=formInputProduk()
	return render(request,'administrasi/inputProduk.html',{'forms':forms})
