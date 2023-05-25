from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

from django.db import transaction

from administrasi.forms import formInputKategori, formInputProduk, UploadFiles
from administrasi.forms import formUpdateProduk

from administrasi.reads import readdata

from django.core.files.base import ContentFile

from administrasi.models import upFiles

from django.conf import settings

import os

from django.contrib import messages
from administrasi.models import Produk, kategoriProduk

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
			messages.success(request,"Data Berhasil Tersimpan!")
		else:
			messages.success(request,"Data Gagal disimpan! Apakah ada duplikat data?")
		
		return HttpResponseRedirect("/adm/input/produk/")	
	forms=formInputProduk()
	return render(request,'administrasi/inputProduk.html',{'forms':forms})

def upload_Produk(request):
	if request.method=="POST":
		myform=UploadFiles(request.POST,request.FILES)
		if myform.is_valid():
			try:
				myform.save()
				####yes bisa!
				mydata = upFiles.objects.all().order_by("-id")[0]
				#dapatkan pathnya dari file
				myfile=os.path.join(settings.BASE_DIR,"media/" + str(mydata.myfile))
				#proses ke insert!
				jumlah_data = readdata.insertToTable(myfile)
				if(jumlah_data==0):
					messages.success(request,"Upload gagal! Apakah ada duplikat data atau format file csv salah?")
				else:
					messages.success(request,"Upload Sukses, ditambahkan %i data!"%jumlah_data)
			except:
				messages.success(request,"Ini file CSV bung bukan gambar euy!!!")
	return HttpResponseRedirect("/adm/input/produk/")

def viewProduk(request):
	mydata = Produk.objects.all()
	return render(request,'administrasi/tampilProduk.html',{'mydata':mydata})

def updateProduk(request,produk_kode):
	mydata = Produk.objects.get(produk_kode=produk_kode)

	if request.method=="POST":
		myforms = formUpdateProduk(request.POST, request.FILES,instance=mydata)
		if myforms.is_valid():
			myforms.save()
			messages.success(request,"data berhasil diupdate!")
			return HttpResponseRedirect('/adm/view/produk')
		else:
			messages.success(request,"data Gagal diupdate! coba cek apakah ada data yang salah?")
	myforms = formUpdateProduk(instance=mydata)
	print(mydata)

	return render(request,'administrasi/updateProduk.html',{'myforms':myforms})

def downTemplateProduk(request):
	#create template data file
	readdata.createTemplateProduk()

	f=open(os.path.join(settings.BASE_DIR,'produk_template.csv'),'r')
	responsenya = HttpResponse(f,content_type="text/plain")
	responsenya['Content-Disposition'] = 'attachment; filename=produk_template.csv'
	return responsenya