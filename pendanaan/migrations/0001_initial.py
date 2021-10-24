# Generated by Django 3.2.7 on 2021-10-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UMKM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merek_bisnis', models.CharField(max_length=50)),
                ('domisili', models.CharField(choices=[('Aceh', 'Aceh'), ('Sumatera Utara', 'Sumatera Utara'), ('Sumatera Barat', 'Sumatera Barat'), ('Riau', 'Riau'), ('Kepulauan Riau', 'Kepulauan Riau'), ('Jambi', 'Jambi'), ('Sumatera Selatan', 'Sumatera Selatan'), ('Kepulauan Bangka Belitung', 'Kepulauan Bangka Belitung'), ('Bengkulu', 'Bengkulu'), ('Lampung', 'Lampung'), ('DKI Jakarta', 'DKI Jakarta'), ('Banten', 'Banten'), ('Jawa Barat', 'Jawa Barat'), ('Jawa Tengah', 'Jawa Tengah'), ('DI Yogyakarta', 'DI Yogyakarta'), ('Jawa Timur', 'Jawa Timur'), ('Bali', 'Bali'), ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'), ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'), ('Kalimantan Barat', 'Kalimantan Barat'), ('Kalimantan Tengah', 'Kalimantan Tengah'), ('Kalimantan Selatan', 'Kalimantan Selatan'), ('Kalimantan Timur', 'Kalimantan Timur'), ('Kalimantan Utara', 'Kalimantan Utara'), ('Sulawesi Utara', 'Sulawesi Utara'), ('Gorontalo', 'Gorontalo'), ('Sulawesi Tengah', 'Sulawesi Tengah'), ('Sulawesi Barat', 'Sulawesi Barat'), ('Sulawesi Selatan', 'Sulawesi Selatan'), ('Sulawesi Tenggara', 'Sulawesi Tenggara'), ('Maluku', 'Maluku'), ('Maluku Utara', 'Maluku Utara'), ('Papua Barat', 'Papua Barat'), ('Papua', 'Papua')], default='Aceh', max_length=30)),
                ('produk_jasa', models.CharField(max_length=30)),
                ('pendanaan_dibutuhkan', models.IntegerField()),
                ('deskripsi', models.TextField()),
                ('logo_usaha', models.ImageField(upload_to='')),
                ('gambar_usaha', models.ImageField(upload_to='')),
                ('ringkasan_perusahaan', models.FileField(upload_to='')),
            ],
        ),
    ]