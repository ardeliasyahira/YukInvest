from django.db import models
from django.contrib.auth.models import User

class UMKM(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    ACEH = 'Aceh'
    SUMATERA_UTARA = 'Sumatera Utara'
    SUMATERA_BARAT = 'Sumatera Barat'
    RIAU = 'Riau'
    KEPULAUAN_RIAU = 'Kepulauan Riau'
    JAMBI = 'Jambi'
    SUMATERA_SELATAN = 'Sumatera Selatan'
    BANGKA_BELITUNG = 'Kepulauan Bangka Belitung'
    BENGKULU = 'Bengkulu'
    LAMPUNG = 'Lampung'
    DKI_JAKARTA = 'DKI Jakarta'
    BANTEN = 'Banten'
    JAWA_BARAT = 'Jawa Barat'
    JAWA_TENGAH = 'Jawa Tengah'
    YOGYAKARTA = 'DI Yogyakarta'
    JAWA_TIMUR = 'Jawa Timur'
    BALI = 'Bali'
    NUSA_TENGGARA_BARAT = 'Nusa Tenggara Barat'
    NUSA_TENGGARA_TIMUR = 'Nusa Tenggara Timur'
    KALIMANTAN_BARAT = 'Kalimantan Barat'
    KALIMANTAN_TENGAH = 'Kalimantan Tengah'
    KALIMANTAN_SELATAN = 'Kalimantan Selatan'
    KALIMANTAN_TIMUR = 'Kalimantan Timur'
    KALIMANTAN_UTARA = 'Kalimantan Utara'
    SULAWESI_UTARA = 'Sulawesi Utara'
    GORONTALO = 'Gorontalo'
    SULAWESI_TENGAH = 'Sulawesi Tengah'
    SULAWESI_BARAT = 'Sulawesi Barat'
    SULAWESI_SELATAN = 'Sulawesi Selatan'
    SULAWESI_TENGGARA = 'Sulawesi Tenggara'
    MALUKU = 'Maluku'
    MALUKU_UTARA = 'Maluku Utara'
    PAPUA_BARAT = 'Papua Barat'
    PAPUA = 'Papua'

    PILIHAN_DOMISILI = [
        (ACEH, 'Aceh'),
        (SUMATERA_UTARA, 'Sumatera Utara'),
        (SUMATERA_BARAT, 'Sumatera Barat'),
        (RIAU, 'Riau'),
        (KEPULAUAN_RIAU, 'Kepulauan Riau'),
        (JAMBI, 'Jambi'),
        (SUMATERA_SELATAN, 'Sumatera Selatan'),
        (BANGKA_BELITUNG, 'Kepulauan Bangka Belitung'),
        (BENGKULU, 'Bengkulu'),
        (LAMPUNG, 'Lampung'),
        (DKI_JAKARTA, 'DKI Jakarta'),
        (BANTEN, 'Banten'),
        (JAWA_BARAT, 'Jawa Barat'),
        (JAWA_TENGAH, 'Jawa Tengah'),
        (YOGYAKARTA, 'DI Yogyakarta'),
        (JAWA_TIMUR, 'Jawa Timur'),
        (BALI, 'Bali'),
        (NUSA_TENGGARA_BARAT, 'Nusa Tenggara Barat'),
        (NUSA_TENGGARA_TIMUR, 'Nusa Tenggara Timur'),
        (KALIMANTAN_BARAT, 'Kalimantan Barat'),
        (KALIMANTAN_TENGAH, 'Kalimantan Tengah'),
        (KALIMANTAN_SELATAN, 'Kalimantan Selatan'),
        (KALIMANTAN_TIMUR, 'Kalimantan Timur'),
        (KALIMANTAN_UTARA, 'Kalimantan Utara'),
        (SULAWESI_UTARA, 'Sulawesi Utara'),
        (GORONTALO, 'Gorontalo'),
        (SULAWESI_TENGAH, 'Sulawesi Tengah'),
        (SULAWESI_BARAT, 'Sulawesi Barat'),
        (SULAWESI_SELATAN, 'Sulawesi Selatan'),
        (SULAWESI_TENGGARA, 'Sulawesi Tenggara'),
        (MALUKU, 'Maluku'),
        (MALUKU_UTARA, 'Maluku Utara'),
        (PAPUA_BARAT, 'Papua Barat'),
        (PAPUA, 'Papua')
    ]

    merek_bisnis = models.CharField(max_length=50)
    domisili = models.CharField(
	max_length=30,
	choices = PILIHAN_DOMISILI,
	default = ACEH
    )

    produk_jasa = models.CharField(max_length=30)
    pendanaan_dibutuhkan = models.IntegerField()
    deskripsi = models.TextField()
    logo_usaha = models.ImageField(upload_to='Logo UMKM/')
    gambar_usaha = models.ImageField(upload_to='Foto UMKM/')
    ringkasan_perusahaan = models.FileField(upload_to='Ringkasan UMKM/')

    dana_terkumpul = 0
    jumlah_investor = 0
    status = "Menunggu"

    def __str__(self):
        return f"{self.merek_bisnis} {self.status}"


    


