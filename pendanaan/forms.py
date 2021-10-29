from django.forms import ModelForm, widgets
from django.forms.widgets import Input, Select, Textarea
from .models import UMKM

class UMKMForm(ModelForm):
    class Meta:
        model = UMKM
        fields = [
	    'merek_bisnis', 'domisili', 'produk_jasa', 'pendanaan_dibutuhkan', 'deskripsi',
	    'logo_usaha', 'gambar_usaha', 'ringkasan_perusahaan'
	]
        widgets = {
            "merek_bisnis": Input(attrs={"class": "form-control"}),
            "domisili": Select(attrs={"class": "form-control"}, choices=(UMKM.PILIHAN_DOMISILI)),
            "produk_jasa": Input(attrs={"class": "form-control"}),
            "pendanaan_dibutuhkan": Input(attrs={"type": "number", "class": "form-control"}),
            "deskripsi": Textarea(attrs={"class": "form-control"}),
            "logo_usaha": Input(attrs={"type": "file", "class": "form-control"}),
            "gambar_usaha": Input(attrs={"type": "file", "class": "form-control"}),
            "ringkasan_perusahaan": Input(attrs={"type": "file", "class": "form-control"}),	    
        }


  