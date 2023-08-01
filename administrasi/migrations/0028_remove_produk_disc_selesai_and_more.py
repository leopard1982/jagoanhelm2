# Generated by Django 4.2.3 on 2023-07-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0027_alter_kategoriproduk_options_alter_produk_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produk',
            name='disc_selesai',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='gratis_ongkir_selesai',
        ),
        migrations.AddField(
            model_name='produk',
            name='disc_active',
            field=models.BooleanField(blank=True, null=True, verbose_name='Discount Aktif?'),
        ),
        migrations.AddField(
            model_name='produk',
            name='gratis_ongkir_active',
            field=models.BooleanField(blank=True, null=True, verbose_name='Gratis Ongkir Aktif?'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='disc',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumlah Discount (dalam Rupiah)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gratis_ongkir',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumlah Gratis Ongkir (dalam Rupiah)'),
        ),
    ]