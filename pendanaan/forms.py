from django.forms import ModelForm, widgets
from django.forms.widgets import Input, Select, Textarea, FileInput
from .models import UMKM

class UMKMForm(ModelForm):
    class Meta:
        model = UMKM
        fields = [
	    'merek_bisnis', 'domisili', 'produk_jasa', 'saham_umkm', 'pendanaan_dibutuhkan', 
	    'deskripsi', 'logo_usaha', 'gambar_usaha', 'ringkasan_perusahaan', 
	]

# 
# "type": "file",
        widgets = {
            "merek_bisnis": Input(attrs={"class": "form-control"}),
            "domisili": Select(attrs={"class": "form-control"}, choices=(UMKM.PILIHAN_DOMISILI)),
            "produk_jasa": Input(attrs={"class": "form-control"}),
	    "saham_umkm": Input(attrs={"class": "form-control"}),
            "pendanaan_dibutuhkan": Input(attrs={"type": "number", "class": "form-control"}),
            "deskripsi": Textarea(attrs={"class": "form-control"}),
            "logo_usaha": FileInput(attrs={"class": "form-control"}),
            "gambar_usaha": FileInput(attrs={"class": "form-control"}),
            "ringkasan_perusahaan": FileInput(attrs={"class": "form-control"}),	    
        }


  