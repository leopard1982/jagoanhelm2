# Generated by Django 4.2.1 on 2023-07-31 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0035_uploadmasterkota_alter_uploadmasterprovinsi_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='masterKota',
            fields=[
                ('kode_kota', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='Kode Kota (angka)')),
                ('nama_kota', models.CharField(max_length=200, verbose_name='Nama Kota')),
                ('kode_provinsi', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrasi.masterprovinsi', verbose_name='Kode Provinsi')),
            ],
            options={
                'ordering': ['kode_kota'],
            },
        ),
    ]
