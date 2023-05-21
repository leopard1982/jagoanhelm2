from django.db import models

# Create your models here.
class kategoriProduk(models.Model):
	nama = models.CharField(max_length=100,verbose_name="Nama Kategori:",primary_key=True,blank=False,null=False)
	deskripsi = models.CharField(max_length=100,verbose_name="Deskripsi Kategori")

	def __str__ (self):
		return self.nama
