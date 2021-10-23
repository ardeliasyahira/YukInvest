from django.forms import ModelForm
from .models import UMKM

class UMKMForm(ModelForm):
    class Meta:
        model = UMKM
        fields = [
	    'merek_bisnis', 'domisili', 'produk_jasa', 'pendanaan_dibutuhkan', 'deskripsi',
	    'logo_usaha', 'gambar_usaha', 'ringkasan_perusahaan'
	]


  