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