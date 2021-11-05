from django import forms
from .models import EditProfil

class moform(forms.ModelForm):
    class Meta:
        model = EditProfil
        fields ='__all__'

