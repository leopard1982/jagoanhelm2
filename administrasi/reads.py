from django.conf import settings
import os
from django.db import transaction
from administrasi.models import kategoriProduk, Produk

@transaction.atomic
class readdata:
	#goyang mang!!!
	def insertToTable(pathnya):
		x=[]

		jumlah_data=0

		file = open(pathnya,'r')
		for mydata in file:
			try:
				y = {
					'kategori_id':mydata.split(',')[0].strip(),
					'produk_kode':mydata.split(',')[1].strip(),
					'produk_nama':mydata.split(',')[2].strip(),
					'produk_serial':mydata.split(',')[3].strip(),
					'produk_produsen':mydata.split(',')[4].strip()
					}
				x.append(y)
			except:
				pass			

		for xx in x:
			try:
				mypro = Produk.objects.create(
						kategori_id=kategoriProduk.objects.get(kategori=xx['kategori_id']),
						produk_kode=xx['produk_kode'],
						produk_nama=xx['produk_nama'],
						produk_serial=xx['produk_serial'],
						produk_produsen=xx['produk_produsen']
					)
				jumlah_data +=1
				
			except:
				pass
		return jumlah_data


	def createTemplateProduk():
		mykategori = kategoriProduk.objects.all()
		kategorinya=""
		for kat in mykategori:
			kategorinya=kategorinya + kat.kategori + "/ "

		f = open(os.path.join(settings.BASE_DIR,'produk_template.csv'),'w')
		f.write("----awal bagian untuk dihapus sebelum upload----\n")
		f.write("Silakan Isikan dengan format di bawah ini menggunakan koma\n")
		f.write("Untuk Pilihan Kategori Bisa ditulis %s (pilih salah satu\n"%kategorinya)
		f.write("Untuk Pilihan Negara Asal Bisa ditulis: Indonesia/Tiongkok/Eropa/Amerika (pilih salah satu)\n")
		f.write("----akhir bagian untuk dihapus sebelum upload----\n")
		f.write("kategori,kode_sku,nama_produk,merek_produk,asal_produk,stok_awal\n")
		f.close()