from django import forms
from django.db.models import fields
from pendanaan.models import UMKM

class UmkmForm(forms.ModelForm):
    class Meta:
        model = UMKM
        fields = '__all__'