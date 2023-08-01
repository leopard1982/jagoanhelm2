# Generated by Django 4.2.1 on 2023-07-31 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0038_alter_masterdesa_options_alter_masterdesa_nama_desa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterdesa',
            name='id',
        ),
        migrations.AlterField(
            model_name='masterdesa',
            name='kode_desa',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='Kode Desa (angka):'),
        ),
    ]