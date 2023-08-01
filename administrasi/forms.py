from django.forms import ModelForm
from django import forms
from administrasi.models import kategoriProduk, Produk, upFiles, upFilesKategori
from administrasi.models import rusakProduk, revisiProduk, bannerToko
from django.db.models import F
from administrasi.models import masterProvinsi, uploadMasterProvinsi, uploadMasterKota
from administrasi.models import masterKota, masterDesa, uploadMasterDesa


class formInputKategori(ModelForm):
    class Meta:
        model = kategoriProduk
        fields = ["kategori", "deskripsi", "gambar"]

        widgets = {
            'kategori': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'gambar': forms.FileInput(attrs={'class': 'form-control'})
        }


class formUpdateKategori(ModelForm):
    class Meta:
        model = kategoriProduk
        fields = ["kategori", "deskripsi", "gambar"]

        widgets = {
            'kategori': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'deskripsi': forms.TextInput(attrs={'class': 'form-control'}),
            'gambar': forms.FileInput(attrs={'class': 'form-control'})
        }


class formInputProduk(ModelForm):
    class Meta:
        model = Produk
        fields = ['kategori', 'produk_kode', 'produk_nama', 'produk_merek', 'produk_asal', 'stok_awal', 'gambar', 'gambar1',
                  'gambar2', 'gambar3', 'berat', 'deskripsi', 'harga']

        widgets = {
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'produk_kode': forms.TextInput(attrs={'class': 'form-control'}),
            'produk_nama': forms.TextInput(attrs={'class': 'form-control'}),
            'produk_merek': forms.TextInput(attrs={'class': 'form-control'}),
            'produk_asal': forms.Select(attrs={'class': 'form-control'}),
            'stok_awal': forms.NumberInput(attrs={'class': 'form-control'}),
            'gambar': forms.FileInput(attrs={'class': 'form-control'}),
            'gambar1': forms.FileInput(attrs={'class': 'form-control'}),
            'gambar2': forms.FileInput(attrs={'class': 'form-control'}),
            'gambar3': forms.FileInput(attrs={'class': 'form-control'}),
            'berat': forms.NumberInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class formUpdateProduk(ModelForm):
    class Meta:
        model = Produk
        fields = ['produk_kode', 'produk_nama', 'produk_merek', 'produk_asal', 'stok_awal', 'stok_masuk', 'stok_revisi', 'stok_rusak', 'stok_akhir', 'gambar', 'gambar1',
                  'gambar2', 'gambar3', 'berat', 'deskripsi', 'harga', 'aktif', 'disc', 'disc_active',
                  'gratis_ongkir', 'gratis_ongkir_active', 'kelengkapan_produk', 'dimensi_produk', 'set_new']

        widgets = {
            'produk_kode': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'produk_nama': forms.TextInput(attrs={'class': 'form-control'}),
            'produk_merek': forms.TextInput(attrs={'class': 'form-control'}),
            'produk_asal': forms.Select(attrs={'class': 'form-select'}),
            'stok_awal': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'stok_masuk': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'stok_revisi': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'stok_rusak': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'stok_akhir': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'gambar': forms.FileInput(attrs={'class': 'form-control'}),
            'gambar1': forms.FileInput(attrs={'class': 'form-control'}),
            'gambar2': forms.FileInput(attrs={'class': 'form-control'}),
            'gambar3': forms.FileInput(attrs={'class': 'form-control'}),
            'berat': forms.NumberInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),
            'kelengkapan_produk': forms.TextInput(attrs={'class': 'form-control'}),
            'dimensi_produk': forms.TextInput(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),
            'disc': forms.NumberInput(attrs={'class': 'form-control'}),
            'gratis_ongkir': forms.NumberInput(attrs={'class': 'form-control'}),
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
        fields = ['produk_kode', 'aktif']


class FormInputStokRusak(ModelForm):
    class Meta:
        model = rusakProduk
        fields = ['id', 'produk_kode', 'jumlah_rusak',
                  'jumlah_ready', 'jumlah_akhir', 'keterangan']

        widgets = {
            'produk_kode': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }),
            'jumlah_rusak': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'jumlah_ready': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'jumlah_akhir': forms.NumberInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }),
            'keterangan': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }


class FormUpdateStokRusak(ModelForm):
    class Meta:
        model = rusakProduk
        fields = ['id', 'produk_kode', 'jumlah_rusak',
                  'jumlah_ready', 'jumlah_akhir', 'keterangan', 'selesai']

        widgets = {
            'id': forms.NumberInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }),
            'produk_kode': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }),
            'jumlah_rusak': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'jumlah_ready': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'jumlah_akhir': forms.NumberInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }),
            'keterangan': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }


class FormInputRevisiStok(ModelForm):
    class Meta:
        model = revisiProduk
        fields = ['produk_kode', 'jumlah_revisi', 'keterangan', 'selesai']

        widgets = {
            'produk_kode': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly'
            }),
            'jumlah_revisi': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'keterangan': forms.Textarea(attrs={
                'class': 'form-control',
                'required': 'required',
            }),
        }


class FormInputBanner(ModelForm):
    class Meta:
        model = bannerToko
        fields = ['banner', 'deskripsi']

        widgets = {
            'banner': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'deskripsi': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }


class formProvinsi(forms.ModelForm):
    class Meta:
        model = masterProvinsi
        fields = "__all__"

        widgets = {
            'kode_provinsi': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'kode provinsi, mis.11'}),
            'nama_provinsi': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'nama provinsi'}),
        }


class formKota(forms.ModelForm):
    class Meta:
        model = masterKota
        fields = "__all__"

        widgets = {
            'kode_provinsi': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'kode_kota': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'kode kota, mis.11'}),
            'nama_kota': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'nama kota'}),
        }


class formDesa(forms.ModelForm):
    class Meta:
        model = masterDesa
        fields = "__all__"

        widgets = {
            'kode_provinsi': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'kode_kota': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'kode_desa': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'kode desa, mis.11'}),
            'nama_desa': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'nama desa'}),
        }

    def __init__(self, kode_provinsi=None, **kwargs):
        super(formDesa, self).__init__(**kwargs)
        if kode_provinsi:
            self.fields['kode_kota'].queryset = masterKota.objects.filter(
                kode_provinsi=kode_provinsi)


class formDesa_save(forms.ModelForm):
    class Meta:
        model = masterDesa
        fields = "__all__"

        widgets = {
            'kode_provinsi': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'kode_kota': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'kode_desa': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'kode desa, mis.11'}),
            'nama_desa': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'nama desa'}),
        }


class formFileProvinsi(forms.ModelForm):
    class Meta:
        model = uploadMasterProvinsi
        fields = "__all__"


class formFileKota(forms.ModelForm):
    class Meta:
        model = uploadMasterKota
        fields = "__all__"


class formFileDesa(forms.ModelForm):
    class Meta:
        model = uploadMasterDesa
        fields = "__all__"
