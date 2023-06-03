from django.forms import ModelForm
from django import forms
from administrasi.models import kategoriProduk, Produk, upFiles, upFilesKategori
from administrasi.models import rusakProduk, revisiProduk, bannerToko
from django.db.models import F

class formInputKategori(ModelForm):
	class Meta:
		model = kategoriProduk
		fields = ["kategori","deskripsi","gambar"]

		widgets = {
			'kategori':forms.TextInput(attrs={'class':'form-control'}),
			'deskripsi':forms.Textarea(attrs={
				'class':'form-control'
				}),
			'gambar': forms.FileInput(attrs={'class':'form-control'})
		}

class formUpdateKategori(ModelForm):
	class Meta:
		model = kategoriProduk
		fields = ["kategori","deskripsi","gambar"]

		widgets = {
			'kategori':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
			'deskripsi':forms.TextInput(attrs={'class':'form-control'}),
			'gambar': forms.FileInput(attrs={'class':'form-control'})
		}


class formInputProduk(ModelForm):
	class Meta:
		model = Produk
		fields = ['kategori','produk_kode','produk_nama','produk_merek','produk_asal','stok_awal','gambar','gambar1','gambar2','gambar3','berat','deskripsi','harga','jumlah1','grosir1','jumlah2','grosir2','jumlah3','grosir3']
		
		widgets = {
			'kategori':forms.Select(attrs={'class':'form-control'}),
			'produk_kode':forms.TextInput(attrs={'class':'form-control'}),
			'produk_nama':forms.TextInput(attrs={'class':'form-control'}),
			'produk_merek':forms.TextInput(attrs={'class':'form-control'}),
			'produk_asal':forms.Select(attrs={'class':'form-control'}),
			'stok_awal':forms.NumberInput(attrs={'class':'form-control'}),
			'gambar':forms.FileInput(attrs={'class':'form-control'}),
			'gambar1':forms.FileInput(attrs={'class':'form-control'}),
			'gambar2':forms.FileInput(attrs={'class':'form-control'}),
			'gambar3':forms.FileInput(attrs={'class':'form-control'}),
			'berat':forms.NumberInput(attrs={'class':'form-control'}),
			'deskripsi':forms.Textarea(attrs={'class':'form-control'}),
			'harga':forms.NumberInput(attrs={'class':'form-control'}),
			'jumlah1':forms.NumberInput(attrs={'class':'form-control'}),
			'grosir1':forms.NumberInput(attrs={'class':'form-control'}),
			'jumlah2':forms.NumberInput(attrs={'class':'form-control'}),
			'grosir2':forms.NumberInput(attrs={'class':'form-control'}),
			'jumlah3':forms.NumberInput(attrs={'class':'form-control'}),
			'grosir3':forms.NumberInput(attrs={'class':'form-control'}),
		}

class formUpdateProduk(ModelForm):
	class Meta:
		model = Produk
		fields = ['produk_kode','produk_nama','produk_merek','produk_asal','stok_awal','stok_masuk','stok_revisi','stok_rusak','stok_akhir','gambar','gambar1','gambar2','gambar3','berat','deskripsi','harga','jumlah1','grosir1','jumlah2','grosir2','jumlah3','grosir3','aktif']
		
		widgets = {
			'produk_kode':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
			'produk_nama':forms.TextInput(attrs={'class':'form-control'}),
			'produk_merek':forms.TextInput(attrs={'class':'form-control'}),
			'produk_asal':forms.Select(attrs={'class':'form-control'}),
			'stok_awal':forms.NumberInput(attrs={'class':'form-control','readonly':'readonly'}),
			'stok_masuk':forms.NumberInput(attrs={'class':'form-control','readonly':'readonly'}),
			'stok_revisi':forms.NumberInput(attrs={'class':'form-control','readonly':'readonly'}),
			'stok_rusak':forms.NumberInput(attrs={'class':'form-control','readonly':'readonly'}),
			'stok_akhir':forms.NumberInput(attrs={'class':'form-control','readonly':'readonly'}),
			'gambar':forms.FileInput(attrs={'class':'form-control'}),
			'gambar1':forms.FileInput(attrs={'class':'form-control'}),
			'gambar2':forms.FileInput(attrs={'class':'form-control'}),
			'gambar3':forms.FileInput(attrs={'class':'form-control'}),
			'berat':forms.NumberInput(attrs={'class':'form-control'}),
			'deskripsi':forms.Textarea(attrs={'class':'form-control'}),
			'harga':forms.NumberInput(attrs={'class':'form-control'}),
			'jumlah1':forms.NumberInput(attrs={'class':'form-control'}),
			'grosir1':forms.NumberInput(attrs={'class':'form-control'}),
			'jumlah2':forms.NumberInput(attrs={'class':'form-control'}),
			'grosir2':forms.NumberInput(attrs={'class':'form-control'}),
			'jumlah3':forms.NumberInput(attrs={'class':'form-control'}),
			'grosir3':forms.NumberInput(attrs={'class':'form-control'}),
		}


class UploadFiles(ModelForm):
	class Meta:
		model = upFiles
		fields = ["myfile",]


class UploadFilesKategori(ModelForm):
	class Meta:
		model = upFilesKategori
		fields = ["myfile",]

class UpdateAktifProduk(ModelForm):
	class Meta:
		model = Produk
		fields= ['produk_kode','aktif']

class FormInputStokRusak(ModelForm):
	class Meta:
		model = rusakProduk
		fields = ['id','produk_kode','jumlah_rusak','jumlah_ready','jumlah_akhir','keterangan']
		
		widgets = {
			'produk_kode': forms.TextInput(attrs={
				'class':'form-control',
				'readonly':'readonly'
				}),
			'jumlah_rusak': forms.NumberInput(attrs={
				'class':'form-control'
				}),
			'jumlah_ready': forms.NumberInput(attrs={
				'class':'form-control'
				}),
			'jumlah_akhir': forms.NumberInput(attrs={
				'class':'form-control',
				'readonly':'readonly'
				}),
			'keterangan': forms.Textarea(attrs={
				'class':'form-control'
				}),
		}

class FormUpdateStokRusak(ModelForm):
	class Meta:
		model = rusakProduk
		fields = ['id','produk_kode','jumlah_rusak','jumlah_ready','jumlah_akhir','keterangan','selesai']
		
		widgets = {
			'id':forms.NumberInput(attrs={
				'class':'form-control',
				'readonly':'readonly'
				}),
			'produk_kode': forms.TextInput(attrs={
				'class':'form-control',
				'readonly':'readonly'
				}),
			'jumlah_rusak': forms.NumberInput(attrs={
				'class':'form-control'
				}),
			'jumlah_ready': forms.NumberInput(attrs={
				'class':'form-control'
				}),
			'jumlah_akhir': forms.NumberInput(attrs={
				'class':'form-control',
				'readonly':'readonly'
				}),
			'keterangan': forms.Textarea(attrs={
				'class':'form-control'
				})
		}

class FormInputRevisiStok(ModelForm):
	class Meta:
		model = revisiProduk
		fields = ['produk_kode','jumlah_revisi','keterangan','selesai']
		
		widgets = {
			'produk_kode': forms.TextInput(attrs={
				'class':'form-control',
				'readonly':'readonly'
				}),
			'jumlah_revisi': forms.NumberInput(attrs={
				'class':'form-control'
				}),
			'keterangan': forms.Textarea(attrs={
				'class':'form-control',
				'required':'required',
				}),
		}

class FormInputBanner(ModelForm):
	class Meta:
		model = bannerToko
		fields = ['banner','deskripsi']

		widgets = {
		'banner': forms.FileInput(attrs={
			'class':'form-control'
			}),
		'deskripsi': forms.Textarea(attrs={
			'class':'form-control'
			}),
		}