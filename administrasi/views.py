from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

from django.db import transaction

from administrasi.forms import formInputKategori, formInputProduk, UploadFiles

from administrasi.reads import readdata

from django.core.files.base import ContentFile

from administrasi.models import upFiles

from django.conf import settings

import os

from django.contrib import messages

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

def upload_Produk(request):
	if request.method=="POST":
		myform=UploadFiles(request.POST,request.FILES)
		if myform.is_valid():
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
	return HttpResponseRedirect("/adm/input/produk/")