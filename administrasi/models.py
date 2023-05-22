from django.db import models

# Create your models here.
class kategoriProduk(models.Model):
	kategori = models.CharField(max_length=100,verbose_name="Nama Kategori:",primary_key=True,blank=False,null=False)
	deskripsi = models.CharField(max_length=100,verbose_name="Deskripsi Kategori")
	gambar = models.ImageField(verbose_name="Gambar Kategori",null=True,upload_to="kategori")
	def __str__ (self):
		return self.kategori


class Produk(models.Model):
	kategori = models.ForeignKey(kategoriProduk,on_delete=models.CASCADE,null=False,blank=False)
	produk_kode =models.CharField(max_length=100,verbose_name='Kode Produk',null=False,blank=False)
	produk_nama =models.CharField(max_length=200,verbose_name='Nama Produk',null=False,blank=False)
	produk_serial = models.CharField(max_length=200,verbose_name='Serial Kode Produk',null=True,blank=True)
	produk_produsen = models.CharField(max_length=200,verbose_name='Produken Produk',null=True,blank=True)
	stok_awal = models.IntegerField(default=0,verbose_name='Stok Awal')
	stok_masuk = models.IntegerField(default=0,verbose_name='Stok Masuk')
	stok_keluar = models.IntegerField(default=0,verbose_name='Stok Keluar')
	stok_rusak = models.IntegerField(default=0,verbose_name="Stok Rusak")
	stok_akhir = models.IntegerField(default=0,verbose_name='Stok Akhir')
	gambar = models.ImageField(verbose_name="Gambar Produk",null=True,upload_to="produk")

	def __str__(self):
		return self.produk_nama
