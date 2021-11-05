from django import forms
from pendanaan.models import UMKM


class SearchForm(forms.ModelForm):
    class Meta:
        model = UMKM
        fields = ['merek_bisnis', 'produk_jasa', 'domisili']
