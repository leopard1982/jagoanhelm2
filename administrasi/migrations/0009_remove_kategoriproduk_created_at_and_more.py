# Generated by Django 4.2.1 on 2023-05-22 17:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("administrasi", "0008_kategoriproduk_created_at_produk_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="kategoriproduk",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="produk",
            name="created_at",
        ),
    ]
