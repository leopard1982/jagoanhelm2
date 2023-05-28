from django.forms import ModelForm
from django import forms
from administrasi.models import kategoriProduk, Produk, upFiles, upFilesKategori

class formInputKategori(ModelForm):
	class Meta:
		model = kategoriProduk
		fields = ["kategori","deskripsi","gambar"]

		widgets = {
			'kategori':forms.TextInput(attrs={'class':'form-control'}),
			'deskripsi':forms.TextInput(attrs={'class':'form-control'}),
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
		fields = ['kategori','produk_kode','produk_nama','produk_merek','produk_asal','stok_awal','stok_rusak','gambar','gambar1','gambar2','gambar3','berat','deskripsi','harga','jumlah1','grosir1','jumlah2','grosir2','jumlah3','grosir3']
		
		widgets = {
			'kategori':forms.Select(attrs={'class':'form-control'}),
			'produk_kode':forms.TextInput(attrs={'class':'form-control'}),
			'produk_nama':forms.TextInput(attrs={'class':'form-control'}),
			'produk_merek':forms.TextInput(attrs={'class':'form-control'}),
			'produk_asal':forms.Select(attrs={'class':'form-control'}),
			'stok_awal':forms.NumberInput(attrs={'class':'form-control'}),
			'stok_rusak':forms.NumberInput(attrs={'class':'form-control'}),
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
		fields = ['produk_kode','produk_nama','produk_merek','produk_asal','stok_awal','stok_rusak','gambar','gambar1','gambar2','gambar3','berat','deskripsi','harga','jumlah1','grosir1','jumlah2','grosir2','jumlah3','grosir3']
		
		widgets = {
			'produk_kode':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
			'produk_nama':forms.TextInput(attrs={'class':'form-control'}),
			'produk_merek':forms.TextInput(attrs={'class':'form-control'}),
			'produk_asal':forms.Select(attrs={'class':'form-control'}),
			'stok_awal':forms.NumberInput(attrs={'class':'form-control'}),
			'stok_rusak':forms.NumberInput(attrs={'class':'form-control'}),
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
