# Generated by Django 4.2.1 on 2023-05-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administrasi", "0012_upfileskategori_alter_produk_gambar_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="produk",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="upfiles",
            name="myfile",
            field=models.FileField(null=True, upload_to="csv_produk"),
        ),
        migrations.AlterField(
            model_name="upfileskategori",
            name="myfile",
            field=models.FileField(null=True, upload_to="csv_kategori"),
        ),
    ]