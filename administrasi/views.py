from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

from django.db import transaction

from administrasi.forms import formInputKategori, formInputProduk, UploadFiles
from administrasi.forms import formUpdateProduk, UploadFilesKategori, formUpdateKategori
from administrasi.forms import UpdateAktifProduk, FormInputStokRusak, FormUpdateStokRusak
from administrasi.forms import FormInputRevisiStok

from administrasi.reads import readdata

from django.core.files.base import ContentFile

from administrasi.models import upFiles, upFilesKategori

from django.conf import settings

from django.core.paginator import Paginator

from django.db.models import Q, F

import os

from django.contrib import messages
from administrasi.models import Produk, kategoriProduk, rusakProduk, revisiProduk

def updateRusakProdukResult():
	x=rusakProduk.objects.all()
	x.update(jumlah_akhir=F('jumlah_rusak')-F('jumlah_ready'))

def updateMasterProduk():
	Produk.objects.all().update(stok_akhir=F('stok_awal')+F('stok_masuk') + F('stok_revisi') -F('stok_keluar')-F('stok_rusak'))
	Produk.objects.all().filter(Q(stok_masuk__gt=0) | Q(stok_keluar__gt=0) | Q(stok_rusak__gt=0) | Q(stok_revisi__gt=0)).update(ada_transaksi=True)
# Create your views here.

def dashboard(request):
	jumlah_produk = Produk.objects.all().count()
	lima_stok = Produk.objects.all().order_by("-created_at")[0:5]
	jumlah_kategori = kategoriProduk.objects.all().count()
	produk_aktif = Produk.objects.all().filter(aktif=True).count()
	produk_nonaktif = Produk.objects.all().filter(aktif=False).count()
	followup_repair = rusakProduk.objects.all().filter(selesai=False).count()
	revisi_stok = revisiProduk.objects.all().filter(selesai=False).count()
	return render(request,'administrasi/dashboard.html',{'revisi_stok':revisi_stok,'followup_repair':followup_repair,'produk_aktif':produk_aktif,'produk_nonaktif':produk_nonaktif,'jumlah_produk':jumlah_produk,'jumlah_kategori':jumlah_kategori,'lima_stok':lima_stok})

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
			updateMasterProduk()
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
				messages.success(request,"Produk dengan kode %s gagal dihapus karena sudah pernah ada transaksi."%produk_kode)
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
					updateMasterProduk()
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
			mydata=mydata.filter(Q(produk_kode__icontains=request.POST['filter']) | Q(produk_merek__icontains=request.POST['filter']) | Q(produk_asal__icontains=request.POST['filter']) |Q(produk_nama__icontains=request.POST['filter']))	
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
			updateMasterProduk()
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

@transaction.atomic()
def inputStokRusak(request,produk_kode):
	if request.method=="POST":
		forms = FormInputStokRusak(request.POST)
		if forms.is_valid():
			forms.save()
			updateRusakProdukResult() #untuk update table rusakProduk
			messages.success(request,"Permintaan Pengajuan Stok Rusak diterima!")
		else:
			messages.success(request,"Permintaan Pengajuan Stok Rusak gagal!")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	#karena FK -> ambil data dari PK
	mydata = Produk.objects.get(produk_kode=produk_kode)
	forms = FormInputStokRusak(instance=mydata)
	return render(request,'administrasi/inputRusak.html',{'forms':forms})

@transaction.atomic()
def updateStokRusak(request,pk):
	if request.method=="POST":
		try:
			mydata = rusakProduk.objects.get(id=pk)
			jumlah_rusak = int(request.POST['jumlah_rusak'])
			jumlah_ready = int(request.POST['jumlah_ready'])
			jumlah_akhir = jumlah_rusak - jumlah_ready
			produk_kode = request.POST['produk_kode']
			keterangan = request.POST['keterangan']

			if jumlah_rusak < jumlah_ready:
				messages.success(request,"Update Stok Rusak Gagal Karena Jumlah Stok Ready > Jumlah Stok Rusak")
			else:
				if Produk.objects.get(produk_kode=produk_kode).stok_akhir > jumlah_akhir:			
					try:
						selesai = request.POST['selesai']
						selesai = True
					except:
						selesai = False
					mydata.jumlah_ready = jumlah_ready
					mydata.jumlah_akhir = jumlah_akhir
					mydata.jumlah_rusak = jumlah_rusak
					mydata.keterangan = keterangan
					mydata.save()

					if selesai:
						if rusakProduk.objects.get(id=pk).selesai != True:
							#UPDATE PRODUK TABLE
							rusakProduk.objects.filter(id=pk).update(selesai=True)
							Produk.objects.all().filter(produk_kode=produk_kode).update(stok_rusak = F('stok_rusak')+jumlah_akhir)
							Produk.objects.all().filter(produk_kode=produk_kode).update(stok_akhir = F('stok_akhir')-jumlah_akhir)
							messages.success(request,"Status Repair Stok Selesai!")
						else:
							messages.success(request,"Status Repair Stock nomor Laporan %i Sudah selesai, tidak bisa diajukan ulang!"%pk)
					else:
						messages.success(request,"Update Status Stok Berhasil!")
					return redirect("viewStatusStokRusak")
				else:
					messages.success(request,"Jumlah Stok Rusak Melebihi Jumlah Stok Produk yang Ada! Silakan Perbaiki Inputan Terlebih dahulu!")
		except:
			messages.success(request,"Maaf, Update Status Stok Gagal!")
		return redirect("viewStatusStokRusak")
	mydata = rusakProduk.objects.get(id=pk)
	forms = FormUpdateStokRusak(instance=mydata)
	return render(request,'administrasi/inputRusak.html',{'forms':forms})

def viewStatusStokRusak(request):
	mydata = rusakProduk.objects.all().order_by("-id")

	filternya =""
	if request.method=="POST":
		filternya=request.POST['filter']
	if(filternya!=""):
		mydata = rusakProduk.objects.all().order_by("-id").filter(Q(produk_kode_id=filternya) | Q(keterangan__icontains=filternya))
	p=None

	if mydata.count()>0:
		if filternya=="":
			p=Paginator(mydata,10)
		else:
			p=Paginator(mydata,mydata.count())
	else:
		p=None

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
	return render(request,'administrasi/fuRusak.html',{'page':page})

def deleterusakProduk(request,pk):
	try:
		if rusakProduk.objects.get(id=pk).selesai==False:
			try:
				rusakProduk.objects.get(id=pk).delete()
				messages.success(request,"Laporan Perbaikan Produk dengan nomor %i berhasil dihapus!"%pk)
			except:
				messages.success(request,"Laporan Perbaikan Produk dengan nomor %i gagal dihapus, apakah ada salah memasukkan nomor Pelaporan?"%produk_kode)
		else:
			messages.success(request,"Laporan Perbaikan %i sudah dinyatakan selesai, tidak bisa dihapus!")
	except:
		pass
	return redirect('viewStatusStokRusak')

def UpdateRevisiStokManual(request,pk):
	if request.method=="POST":
		forms = FormInputRevisiStok(request.POST)
		if forms.is_valid():
			revisiProduk.objects.all().filter(id=pk).update(jumlah_revisi = int(request.POST['jumlah_revisi']))
			revisiProduk.objects.all().filter(id=pk).update(keterangan = request.POST['keterangan'])
			selesai=False
			try:
				selesai = request.POST['selesai']
				selesai = True
			except:
				selesai = False

			if(selesai):
				if(revisiProduk.objects.get(id=pk).selesai!=True):
					revisiProduk.objects.all().filter(id=pk).update(selesai = True)
					kode_produk=revisiProduk.objects.get(id=pk).produk_kode.produk_kode

					Produk.objects.all().filter(produk_kode=kode_produk).update(stok_revisi=F('stok_revisi')+int(request.POST['jumlah_revisi']))
					messages.success(request,"Permintaan Pengajuan Revisi selesai diproses!")
					updateMasterProduk()
				else:
					messages.success(request,"Pengajuan Revisi nomor %i sudah Selesai, tidak bisa diajukan ulang!"%pk)
			else:
				messages.success(request,"Permintaan Pengajuan Revisi Jumlah Stok diterima!")
		else:
			messages.success(request,"Permintaan Pengajuan Revisi Jumlah Stok Gagal! Apakah ada salah input kode produk?")
		return HttpResponseRedirect('/adm/view/produk/revisi/')
	#karena FK -> ambil data dari PK
	mydata = revisiProduk.objects.get(id=pk)
	forms = FormInputRevisiStok(instance=mydata)
	return render(request,'administrasi/revisiManual.html',{'forms':forms})

def InputRevisiStokManual(request,produk_kode):
	if request.method=="POST":
		forms = FormInputRevisiStok(request.POST)
		if forms.is_valid():
			forms.save()
			selesai=False
			try:
				selesai = request.POST['selesai']
				selesai = True
			except:
				selesai = False

			if(selesai):
				Produk.objects.all().filter(produk_kode=produk_kode).update(stok_revisi=F('stok_revisi')+int(request.POST['jumlah_revisi']))
				messages.success(request,"Permintaan Pengajuan Revisi selesai diproses!")
				updateMasterProduk()
			else:
				messages.success(request,"Permintaan Pengajuan Revisi Jumlah Stok diterima!")
		else:
			messages.success(request,"Permintaan Pengajuan Revisi Jumlah Stok Gagal! Apakah ada salah input kode produk?")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	#karena FK -> ambil data dari PK
	mydata = Produk.objects.get(produk_kode=produk_kode)
	forms = FormInputRevisiStok(instance=mydata)
	return render(request,'administrasi/revisiManual.html',{'forms':forms})


def viewStatusRevisiStok(request):
	mydata = revisiProduk.objects.all().order_by("-id")
	filternya =""
	if request.method=="POST":
		filternya=request.POST['filter']
	if(filternya!=""):
		mydata = revisiProduk.objects.all().order_by("-id").filter(Q(produk_kode_id=filternya) | Q(keterangan__icontains=filternya))
	p=None

	if mydata.count()>0:
		if filternya=="":
			p=Paginator(mydata,10)
		else:
			p=Paginator(mydata,mydata.count())
	else:
		p=None

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
	return render(request,'administrasi/view_revisi_stok.html',{'page':page})

def deleteRevisiProduk(request,pk):
	try:
		if revisiProduk.objects.get(id=pk).selesai==False:
			try:
				revisiProduk.objects.get(id=pk).delete()
				messages.success(request,"Laporan Revisi Jumlah Stok dengan nomor %i berhasil dihapus!"%pk)
			except:
				messages.success(request,"Laporan Revisi Jumlah Stok dengan nomor %i gagal dihapus, apakah ada salah memasukkan nomor Pelaporan?"%pk)
		else:
			messages.success(request,"Laporan Revisi Jumlah Stok dengan nomor %i sudah dinyatakan selesai, tidak bisa dihapus!"%pk)
	except:
		pass
	return HttpResponseRedirect('/adm/view/produk/revisi/')