from django import forms
from .models import EditProfil

class DataDiriForm(forms.Form):
    PLACE_SELECT= [
        ('wni indo', 'WNI tinggal di Indonesia'),
        ('wni negeri', 'WNI tinggal di luar negeri'),
        ('wna indo', 'WNA tinggal di Indonesia'),
        ('wna negeri', 'WNA tinggal di luar negeri')
    ]

    STATUS_SELECT= [
        ('belum', 'Belum Menikah'),
        ('menikah', 'Menikah'),
        ('other', 'Lainnya')
    ]
    kewarganegaraan = forms.CharField(label='Kewarganegaraan', widget=forms.Select(choices=PLACE_SELECT))
    status = forms.CharField(label='Status Pernikahan', widget=forms.Select(choices=STATUS_SELECT))



class PekerjaanForm(forms.Form):

    PENDAPATAN_SELECT = [
        ('limajuta', '< 5 Juta'),
        ('limampsepuluh', '5-10 Juta'),
        ('lebihsepuluh', '> 10-50 Juta'),
        ('lebihlimapuluh', '> 50-100 Juta'),
        ('lebihseratus', '> 100-500 Juta'),
        ('lebihlimaratus', '> 500 Juta'),
        ('satumil','> 1 Milyar'),
    ]

    PENDAPATAN_SELECT = [
        ('limajuta', '< 5 Juta'),
        ('limampsepuluh', '5-10 Juta'),
        ('lebihsepuluh', '> 10-50 Juta'),
        ('lebihlimapuluh', '> 50-100 Juta'),
        ('lebihseratus', '> 100-500 Juta'),
        ('lebihlimaratus', '> 500 Juta'),
        ('satumil','> 1 Milyar'),
    ]

    SUMBER_SELECT = [
        ('bisnis', 'Bisnis'),
        ('gaji', 'Gaji'),
        ('investasi', 'Investasi'),
        ('tabungan', 'Tabungan'),
        ('deposito', 'Deposito'),
        ('danapensiun', 'Dana Pensiun'),
        ('warisan', 'Warisan'),
        ('lainnya', 'Lainnya')
    ]
    pendapatan = forms.CharField(label='Pendapatan Per Bulan', widget=forms.Select(choices=PENDAPATAN_SELECT))
    sumber = forms.CharField(label='Sumber Pendapatan', widget=forms.Select(choices=SUMBER_SELECT))


class PreferensiForm(forms.Form):
    PENDAPATANYEAH_SELECT = [
        ('limajuta', '< 5 Juta'),
        ('limampsepuluh', '5-10 Juta'),
        ('lebihsepuluh', '> 10-50 Juta'),
        ('lebihlimapuluh', '> 50-100 Juta'),
        ('lebihseratus', '> 100-500 Juta'),
        ('lebihlimaratus', '> 500 Juta'),
        ('satumil','> 1 Milyar'),
    ]

    RESIKO_SELECT = [
        ('rendah', 'Rendah'),
        ('sedang', 'Sedang'),
        ('tinggi', 'Tinggi'),
    ]

    PERAN_SELECT = [
        ('pasif', 'Investasi Pasif'),
        ('owner', 'Owner Operator'),
        ('mengajukan', 'Mengajukan Pendanaan')
    ]

    budgetinvestasi = forms.CharField(label='Budget Investasi', widget=forms.Select(choices=PENDAPATANYEAH_SELECT))
    #cari cara gimana cara ambil multiple selectnya investasi di form (tujuan investasi)
    resiko = forms.CharField(label='Preferensi Resiko Investasi', widget=forms.Select(choices=RESIKO_SELECT))
    #cari cara gimana cara ambil multiple selectnya investasi di form (preferensi investasi)
    prefperan = forms.CharField(label='Preferensi Peran', widget=forms.Select(choices=PERAN_SELECT))

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')


class InvestasiForm(forms.Form):
    OPTIONS = (
        ("pendek", "Investasi Jangka Pendek"),
        ("panjang", "Investasi Jangka Panjang"),
        ("spekulasi", "Spekulasi"),
        ("pendapatan", "Pendapatan"),
    )

    tujuanInvestasi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)

class moform(forms.ModelForm):
    class Meta:
        model = EditProfil
        fields = '__all__'

