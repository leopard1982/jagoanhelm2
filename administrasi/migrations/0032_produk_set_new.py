# Generated by Django 4.2.3 on 2023-07-25 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0031_remove_produk_grosir1_remove_produk_grosir2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produk',
            name='set_new',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Apakah Akan Diset NEW?'),
        ),
    ]