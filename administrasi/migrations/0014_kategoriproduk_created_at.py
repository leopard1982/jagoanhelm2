# Generated by Django 4.2.1 on 2023-05-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administrasi", "0013_produk_created_at_alter_upfiles_myfile_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="kategoriproduk",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
