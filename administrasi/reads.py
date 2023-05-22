from django.conf import settings
import os
from django.db import transaction
from administrasi.models import kategoriProduk, Produk

class readdata:
	def insertToTable():
		x=[]

		file = open(os.path.join(settings.BASE_DIR,'mydata.csv'))
		
		for mydata in file:
			try:
				y = {
				'kategori_id':mydata.split(',')[0],
				'produk_kode':mydata.split(',')[1],
				'produk_nama':mydata.split(',')[2],
				'produk_serial':mydata.split(',')[3],
				'produk_produsen':mydata.split(',')[4]
				}
				x.append(y)
			except:
				pass


		for xx in x:
			try:
				mypro = Produk(
						kategori_id=kategoriProduk.objects.get(kategori=xx['kategori_id']),
						produk_kode=xx['produk_kode'],
						produk_nama=xx['produk_nama'],
						produk_serial=xx['produk_serial'],
						produk_produsen=xx['produk_produsen']
					)
				mypro.save()
			except:
				pass