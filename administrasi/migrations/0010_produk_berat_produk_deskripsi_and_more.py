# Generated by Django 4.2.1 on 2023-05-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administrasi", "0009_remove_kategoriproduk_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="produk",
            name="berat",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Berat dalam gram"
            ),
        ),
        migrations.AddField(
            model_name="produk",
            name="deskripsi",
            field=models.TextField(
                blank=True, null=True, verbose_name="Deskripsi Produk"
            ),
        ),
        migrations.AlterField(
            model_name="produk",
            name="produk_produsen",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Produsen Produk"
            ),
        ),
    ]
