# Generated by Django 4.2.1 on 2023-06-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0023_bannertoko_deskripsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='produk',
            name='disc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='produk',
            name='disc_mulai',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='produk',
            name='disc_selesai',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bannertoko',
            name='deskripsi',
            field=models.TextField(blank=True, null=True, verbose_name='Deskripsi Banner'),
        ),
    ]
