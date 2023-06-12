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
	deskripsi = models.TextField(max_length=100,verbose_name="Deskripsi Kategori",null=False,blank=False)
	gambar = models.ImageField(verbose_name="Gambar Kategori",null=True,upload_to="kategori")
	created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	def __str__ (self):
		return self.kategori


class Produk(models.Model):
	kategori = models.CharField(max_length=100,verbose_name="Kategori Produk",null=False,blank=False)
	produk_kode =models.CharField(max_length=100,verbose_name='Kode Produk',null=False,blank=False,primary_key=True)
	produk_nama =models.CharField(max_length=200,verbose_name='Nama Produk',null=False,blank=False)
	produk_merek = models.CharField(max_length=200,verbose_name='Kode SKU Produk',null=True,blank=True)
	produk_asal = models.CharField(choices=asal_negara, max_length=200,verbose_name='Asal Negara',null=True,blank=True)
	stok_awal = models.IntegerField(default=0,verbose_name='Stok Awal')
	stok_masuk = models.IntegerField(default=0,verbose_name='Stok Masuk')
	stok_revisi = models.IntegerField(default=0,verbose_name="Stok Revisi (Penambahan/ Pengurangan Manual)")
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
	created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	aktif = models.BooleanField(default=True,verbose_name="Klik apabila status Produk Aktif")
	ada_transaksi = models.BooleanField(default=False)
	disc = models.IntegerField(default=0,blank=True,null=True,verbose_name="Jumlah Discount (dalam %)")
	disc_mulai = models.DateField(auto_now_add=False,blank=True,null=True,verbose_name="Tanggal Mulai Discount")
	disc_selesai = models.DateField(auto_now_add=False,blank=True,null=True,verbose_name="Tanggal Selesai Discount")

	def __str__(self):
		return self.produk_nama

class upFiles(models.Model):
	myfile = models.FileField(upload_to="csv_produk",null=True)

class upFilesKategori(models.Model):
	myfile = models.FileField(upload_to="csv_kategori",null=True)

class rusakProduk(models.Model):
	produk_kode = models.ForeignKey(Produk,on_delete=models.RESTRICT,null=False,blank=False,verbose_name="Kode Produk")
	created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	jumlah_rusak = models.IntegerField(default=0,null=False,blank=False,verbose_name="Jumlah Stok Rusak")
	jumlah_ready = models.IntegerField(default=0,null=False,blank=False,verbose_name="Jumlah Stok Diperbaiki/Retur")
	jumlah_akhir = models.IntegerField(default=0,null=False,blank=False,verbose_name="Result Jumlah Stok Akhir Rusak")
	keterangan = models.TextField(max_length=200,verbose_name="Keterangan",null=True,blank=True)
	selesai = models.BooleanField(default=False,blank=False,null=False,verbose_name="Klik apabila status selesai")

	def __str__(self):
		return self.produk_kode

class revisiProduk(models.Model):
	produk_kode = models.ForeignKey(Produk,on_delete=models.RESTRICT,null=False,blank=False,verbose_name="Kode Produk")
	created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	jumlah_revisi = models.IntegerField(default=0,null=False,blank=False,verbose_name="Jumlah Revisi Penambahan/ Pengurangan")
	keterangan = models.TextField(max_length=200,verbose_name="Keterangan",null=True,blank=True)
	selesai = models.BooleanField(default=False,blank=False,null=False,verbose_name="Klik apabila status selesai")

	def __str__(self):
		return self.produk_kode

class bannerToko(models.Model):
	banner = models.ImageField(upload_to="banner",null=True,blank=True,verbose_name="Pilih Gambar untuk Banner")
	deskripsi = models.TextField(null=True,blank=True,verbose_name="Deskripsi Banner")
	def __str__(self):
		return self.deskripsi