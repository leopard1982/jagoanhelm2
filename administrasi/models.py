from django.db import models

# Create your models here.

asal_negara = [
	("Indonesia","Indonesia"),
	("Tiongkok","Tiongkok"),
	("Amerika","Amerika"),
	("Eropa","Eropa")
]

class kategoriProduk(models.Model):
	kategori = models.CharField(max_length=100,verbose_name="Nama Kategori:",primary_key=True,blank=False,null=False)
	deskripsi = models.CharField(max_length=100,verbose_name="Deskripsi Kategori",null=False,blank=False)
	gambar = models.ImageField(verbose_name="Gambar Kategori",null=True,upload_to="kategori")
	
	def __str__ (self):
		return self.kategori


class Produk(models.Model):
	kategori = models.ForeignKey(kategoriProduk,on_delete=models.CASCADE,null=False,blank=False)
	produk_kode =models.CharField(max_length=100,verbose_name='Kode Produk',null=False,blank=False,primary_key=True)
	produk_nama =models.CharField(max_length=200,verbose_name='Nama Produk',null=False,blank=False)
	produk_merek = models.CharField(max_length=200,verbose_name='Kode SKU Produk',null=True,blank=True)
	produk_asal = models.CharField(choices=asal_negara, max_length=200,verbose_name='Asal Negara',null=True,blank=True)
	stok_awal = models.IntegerField(default=0,verbose_name='Stok Awal')
	stok_masuk = models.IntegerField(default=0,verbose_name='Stok Masuk')
	stok_keluar = models.IntegerField(default=0,verbose_name='Stok Keluar')
	stok_rusak = models.IntegerField(default=0,verbose_name="Stok Rusak")
	stok_akhir = models.IntegerField(default=0,verbose_name='Stok Akhir')
	gambar = models.ImageField(verbose_name="Gambar Produk",null=True,upload_to="produk",blank=True)
	gambar1 = models.ImageField(verbose_name="Gambar Produk#1",null=True,upload_to="produk",blank=True)
	gambar2 = models.ImageField(verbose_name="Gambar Produk#2",null=True,upload_to="produk",blank=True)
	gambar3 = models.ImageField(verbose_name="Gambar Produk#3",null=True,upload_to="produk",blank=True)
	berat = models.IntegerField(verbose_name="Berat dalam gram",null=True,blank=True)
	deskripsi = models.TextField(verbose_name="Deskripsi Produk",null=True,blank=True)
	harga = models.IntegerField(verbose_name="Harga Eceran",default=0)
	jumlah1 = models.IntegerField(verbose_name="Jumlah Pembelian Tingkat #1",default=0)
	jumlah2 = models.IntegerField(verbose_name="Jumlah Pembelian Tingkat #2",default=0)
	jumlah3 = models.IntegerField(verbose_name="Jumlah Pembelian Tingkat #3",default=0)
	grosir1 = models.IntegerField(verbose_name="Harga Grosir Tingkat #1",default=0)
	grosir2 = models.IntegerField(verbose_name="Harga Grosir Tingkat #2",default=0)
	grosir3 = models.IntegerField(verbose_name="Harga Grosir Tingkat #3",default=0)

	def __str__(self):
		return self.produk_nama

class upFiles(models.Model):
	myfile = models.FileField(upload_to="csv_produk",null=True)

class upFilesKategori(models.Model):
	myfile = models.FileField(upload_to="csv_kategori",null=True)
