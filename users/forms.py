from django import forms

class AuthForm(forms.Form):
    nama = forms.CharField(
        max_length = 300,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Masukkan username'
            }
        )
    )
    
    password = forms.CharField(
        max_length = 20,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Masukkan password'
            }
        )
    )
