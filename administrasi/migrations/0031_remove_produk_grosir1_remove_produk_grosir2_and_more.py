# Generated by Django 4.2.3 on 2023-07-25 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0030_produk_dimensi_produk_produk_kelengkapan_produk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produk',
            name='grosir1',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='grosir2',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='grosir3',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='jumlah1',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='jumlah2',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='jumlah3',
        ),
    ]
