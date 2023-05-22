from django.forms import ModelForm
from django import forms
from administrasi.models import kategoriProduk, Produk, upFiles

class formInputKategori(ModelForm):
	class Meta:
		model = kategoriProduk
		fields = ["kategori","deskripsi","gambar"]

		widgets = {
			'kategori':forms.TextInput(attrs={'class':'form-control'}),
			'deskripsi':forms.TextInput(attrs={'class':'form-control'})
		}

class formInputProduk(ModelForm):
	class Meta:
		model = Produk
		fields = ["kategori","produk_kode","gambar","produk_nama","produk_serial","produk_produsen","stok_awal"]

		widgets = {
			'produk_kode': forms.TextInput(attrs={'class':'form-control'}),
			'produk_nama': forms.TextInput(attrs={'class':'form-control'}),
			'produk_serial': forms.TextInput(attrs={'class':'form-control'}),
			'produk_produsen': forms.TextInput(attrs={'class':'form-control'}),
			'stok_awal': forms.NumberInput(attrs={'class':'form-control'}),
		}
		# def __init__(self, *args, **kwargs):
		#     super(formInputProduk, self).__init__(*args, **kwargs)
		#     fields['produk_kode'].widget.attrs["class"]="form-control"
		#     fields['produk_nama'].widget.attrs['class']="form-control"
		#     fields['produk_serial'].widget.attrs['class']="form-control"
		#     fields['produk_produsen'].widget.attrs['class']="form-control"
		#     fields['stok_awal'].widget.attrs['class']="form-control"

class UploadFiles(ModelForm):
	class Meta:
		model = upFiles
		fields = ["myfile",]