# Generated by Django 4.2.3 on 2023-07-25 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0026_alter_produk_kategori'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategoriproduk',
            options={'ordering': ['kategori']},
        ),
        migrations.AlterModelOptions(
            name='produk',
            options={'ordering': ['produk_kode']},
        ),
        migrations.AlterModelOptions(
            name='revisiproduk',
            options={'ordering': ['produk_kode']},
        ),
        migrations.AlterModelOptions(
            name='rusakproduk',
            options={'ordering': ['produk_kode']},
        ),
        migrations.RemoveField(
            model_name='produk',
            name='disc_mulai',
        ),
        migrations.AddField(
            model_name='produk',
            name='gratis_ongkir',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumlah Discount (dalam %)'),
        ),
        migrations.AddField(
            model_name='produk',
            name='gratis_ongkir_selesai',
            field=models.DateField(blank=True, null=True, verbose_name='Tanggal Selesai Discount'),
        ),
        migrations.AlterField(
            model_name='bannertoko',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='banner', verbose_name='Pilih Gambar untuk Banner (Ukuran 4:1, misal: panjang 400px, lebar 100px):'),
        ),
    ]
