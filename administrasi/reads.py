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
					'produk_merek':mydata.split(',')[3].strip(),
					'produk_asal':mydata.split(',')[4].strip()
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
						produk_merek=xx['produk_merek'],
						produk_asal=xx['produk_asal']
					)
				jumlah_data +=1
				
			except:
				pass
		file.close()
		os.remove(pathnya)
		return jumlah_data

	def insertToTableKategori(pathnya):
		x=[]

		jumlah_data=0

		file = open(pathnya,'r')
		for mydata in file:
			try:
				y = {
					'kategori':mydata.split(',')[0].strip(),
					'deskripsi':mydata.split(',')[1].strip(),
					}
				x.append(y)
			except:
				pass		

		for xx in x:
			# print("%s %s"%(xx['kategori'],xx['deskripsi']))
			try:
				kategoriProduk.objects.create(kategori=xx['kategori'],deskripsi=xx['deskripsi'])
				jumlah_data+=1
			except:
				pass
		file.close()
		os.remove(pathnya)
		# for xx in x:
		# 	print(xx)
		# 	try:
		# 		mypro = kategoriProduk.objects.create(
		# 				kategori=xx['kategori_id'],
		# 				deskripsi=xx['deskripsi'],
		# 			)
		# 		jumlah_data +=1
				
		# 	except:
		# 		print(mypro)
		return jumlah_data

	def createTemplateProduk():
		jumlah=1;
		mykategori = kategoriProduk.objects.all()
		kategorinya=""
		for kat in mykategori:
			kategorinya=kategorinya + "(%i).%s "%(jumlah,kat.kategori)
			jumlah += 1

		f = open(os.path.join(settings.BASE_DIR,'produk_template.csv'),'w')
		f.write("----awal bagian untuk dihapus sebelum upload----\n")
		f.write("Silakan Isikan dengan format di bawah ini menggunakan koma\n")
		f.write("Untuk Pilihan Kategori Bisa ditulis %s (pilih salah satu)\n"%kategorinya)
		f.write("Untuk Pilihan Negara Asal Bisa ditulis: Indonesia/Tiongkok/Eropa/Amerika (pilih salah satu)\n")
		f.write("----akhir bagian untuk dihapus sebelum upload----\n")
		f.write("kategori,kode_sku,nama_produk,merek_produk,asal_produk,stok_awal\n")
		f.close()

	def createTemplateKategori():
		f = open(os.path.join(settings.BASE_DIR,'kategori_template.csv'),'w')
		f.write("----awal bagian untuk dihapus sebelum upload----\n")
		f.write("Silakan Isikan dengan format di bawah ini menggunakan koma\n")
		f.write("----akhir bagian untuk dihapus sebelum upload----\n")
		f.write("kategori,deskripsi\n")
		f.close()