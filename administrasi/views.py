from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

from django.db import transaction

from administrasi.forms import formInputKategori, formInputProduk, UploadFiles
from administrasi.forms import formUpdateProduk, UploadFilesKategori, formUpdateKategori
from administrasi.forms import UpdateAktifProduk

from administrasi.reads import readdata

from django.core.files.base import ContentFile

from administrasi.models import upFiles, upFilesKategori

from django.conf import settings

from django.core.paginator import Paginator

from django.db.models import Q

import os

from django.contrib import messages
from administrasi.models import Produk, kategoriProduk

# Create your views here.
def dashboard(request):
	jumlah_produk = Produk.objects.all().count()
	lima_stok = Produk.objects.all().order_by("-created_at")[0:5]
	jumlah_kategori = kategoriProduk.objects.all().count()
	produk_aktif = Produk.objects.all().filter(aktif=True).count()
	produk_nonaktif = Produk.objects.all().filter(aktif=False).count()
	return render(request,'administrasi/dashboard.html',{'produk_aktif':produk_aktif,'produk_nonaktif':produk_nonaktif,'jumlah_produk':jumlah_produk,'jumlah_kategori':jumlah_kategori,'lima_stok':lima_stok})

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

def delete_Produk(request,produk_kode):
	try:
		if Produk.objects.get(produk_kode=produk_kode).ada_transaksi==False:
			try:
				Produk.objects.get(produk_kode=produk_kode).delete()
				messages.success(request,"Produk dengan kode %s berhasil dihapus!"%produk_kode)
			except:
				messages.success(request,"Produk dengan kode %s gagal dihapus, apakah ada salah memasukkan kode?"%produk_kode)
		else:
			messages.success(request,"Produk Tidak Dapat dihapus, karena sudah ada transaksi!")
	except:
		pass
	return redirect('viewProduk')

def delete_Kategori(request,kategori):
	try:
		kategoriProduk.objects.get(kategori=kategori).delete()
		messages.success(request,"Kategori Produk %s berhasil dihapus!"%kategori)
	except:
		messages.success(request,"Kategori dengan kode %s gagal dihapus karena sudah memiliki produk!"%kategori)

	return redirect('viewkategoriProduk')

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
				print(myform)
				messages.success(request,"Format file harus csv! Upload dibatalkan!")
	return HttpResponseRedirect("/adm/input/produk/")

def upload_Kategori(request):
	if request.method=="POST":
		myform=UploadFilesKategori(request.POST,request.FILES)
		if myform.is_valid():
			try:
				myform.save()
				####yes bisa!
				mydata = upFilesKategori.objects.all().order_by("-id")[0]
				#dapatkan pathnya dari file
				#print(os.path.join(settings.BASE_DIR,"media/" + str(mydata.myfile)))
				myfile=os.path.join(settings.BASE_DIR,"media/" + str(mydata.myfile))
				#proses ke insert!
				jumlah_data = readdata.insertToTableKategori(myfile)
				if(jumlah_data==0):
					messages.success(request,"Upload gagal! Apakah ada duplikat data atau format file csv salah?")
				else:
					messages.success(request,"Upload Sukses, ditambahkan %i data!"%jumlah_data)
			except:
				messages.success(request,"Format file harus csv! Upload dibatalkan!")
	return HttpResponseRedirect("/adm/input/kategori/")


def viewProduk(request):
	mydata = Produk.objects.all().order_by("-created_at")
	p=Paginator(mydata,5)
	if(request.method=="POST"):
		if request.POST['filter'] != "":
			mydata=mydata.filter(Q(produk_kode__startswith=request.POST['filter']) | Q(produk_merek__startswith=request.POST['filter']) | Q(produk_asal__startswith=request.POST['filter']) |Q(produk_nama__startswith=request.POST['filter']))	
			p=Paginator(mydata,mydata.count())

	halaman=1
	if request.GET.get("p") is not None :
		try:
			halaman=int(request.GET.get("p"))
		except:
			halaman=1
	else:
		halaman=1

	try:
		page = p.get_page(halaman)
	except:
		page = None

	return render(request,'administrasi/tampilProduk.html',{'page':page})

def viewkategoriProduk(request):
	mydata = kategoriProduk.objects.all()
	p=Paginator(mydata,5)
	halaman=1
	if request.GET.get("p") is not None :
		try:
			halaman=int(request.GET.get("p"))
		except:
			halaman=1
	else:
		halaman=1

	try:
		page = p.get_page(halaman)
	except:
		page = None

	return render(request,'administrasi/tampilKategori.html',{'page':page})

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
	

	return render(request,'administrasi/updateProduk.html',{'myforms':myforms})

def updateKategori(request,kategori):
	mydata = kategoriProduk.objects.get(kategori=kategori)

	if request.method=="POST":
		myforms = formUpdateKategori(request.POST, request.FILES,instance=mydata)
		if myforms.is_valid():
			myforms.save()
			messages.success(request,"Data Kategori: %s berhasil diupdate!"%kategori)
			return HttpResponseRedirect('/adm/view/kategoriproduk/')
		else:
			messages.success(request,"Data Kategori %s Gagal diupdate! coba cek apakah ada data yang salah?"%kategori)
	myforms = formUpdateKategori(instance=mydata)
	

	return render(request,'administrasi/updateKategori.html',{'myforms':myforms})

def downTemplateProduk(request):
	#create template data file
	readdata.createTemplateProduk()

	f=open(os.path.join(settings.BASE_DIR,'produk_template.csv'),'r')
	responsenya = HttpResponse(f,content_type="text/plain")
	responsenya['Content-Disposition'] = 'attachment; filename=produk_template.csv'
	return responsenya

def downTemplateKategori(request):
	#create template data file
	readdata.createTemplateKategori()

	f=open(os.path.join(settings.BASE_DIR,'kategori_template.csv'),'r')
	responsenya = HttpResponse(f,content_type="text/plain")
	responsenya['Content-Disposition'] = 'attachment; filename=kategori_template.csv'
	return responsenya

def updateStatusProduk(request):
	produk_kode=request.GET.get('pk')
	produk_status = request.GET.get('st')

	print(produk_status)
	status=True

	if produk_status == "1":
		status=False
	if produk_status== "0":
		status=True


	
	mypro = Produk.objects.get(produk_kode=produk_kode)
	mypro.aktif=status
	mypro.save()
	
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))