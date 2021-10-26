from django import forms
from .models import EditProfil

GENDER_SELECT= [
    ('pria', 'Pria'),
    ('wanita', 'Wanita'),
    ('other', 'Other')
]

PLACE_SELECT= [
    ('wni indo', 'WNI tinggal di Indonesia'),
    ('wni negeri', 'WNI tinggal di luar negeri'),
    ('wna indo', 'WNA tinggal di Indonesia'),
    ('wna negeri', 'WNA tinggal di luar negeri'),
]

STATUS_SELECT= [
    ('belum', 'Belum Menikah'),
    ('menikah', 'Menikah'),
    ('other', 'Lainnya')
]

class DataDiriForm(forms.Form):
    jeniskelamin = forms.CharField(label='Jenis kelamin', widget=forms.Select(choices=GENDER_SELECT))
    kewarganegaraan = forms.CharField(label='Kewarganegaraan', widget=forms.Select(choices=PLACE_SELECT))
    status = forms.CharField(label='Status Pernikahan', widget=forms.Select(choices=STATUS_SELECT))

PT_SELECT= [
    ('sd', 'SD'),
    ('smp', 'SMP'),
    ('sma', 'SMA'), 
    ('sma', 'SMA'),
    ('d3', 'D3'),
    ('s1', 'S1'),
    ('s2', 'S2'),
    ('s3', 'S3'),
    ('lain', 'Lainnya'),
]

WORK_SELECT = [
    ('ks', 'Karyawan Swasta'),
    ('wira', 'Wiraswasta'),
    ('pns', 'Pegawai Negeri Sipil'),
    ('pegawai', 'Pegawai BUMN'),
    ('aparatur', 'Aparatur'),
    ('pensiun', 'Pensiunan'),
    ('guru','Guru'),
    ('irt','Ibu Rumah Tangga'),
    ('pelajar', 'Pelajar'),
    ('lainnya','Lainnya'),
]

INDUSTRI_SELECT = [
    ('retail', 'Retail'),
    ('otomotif', 'Otomotif'),
    ('finansial', 'Finansial'),
    ('travel', 'Travel'),
    ('pendidikan', 'Pendidikan'),
    ('mm', 'Makanan dan Minuman'),
    ('ksd','Kesehatan dan Gaya Hidup'),
    ('penginapan','Penginapan'),
    ('agribisnis', 'Agribisnis'),
    ('pertambangan','Pertambangan'),
    ('lain','Lainnya')
]

INDUSTRI_SELECT = [
    ('retail', 'Retail'),
    ('otomotif', 'Otomotif'),
    ('finansial', 'Finansial'),
    ('travel', 'Travel'),
    ('pendidikan', 'Pendidikan'),
    ('mm', 'Makanan dan Minuman'),
    ('ksd','Kesehatan dan Gaya Hidup'),
    ('penginapan','Penginapan'),
    ('agribisnis', 'Agribisnis'),
    ('pertambangan','Pertambangan'),
    ('lain','Lainnya')
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

class PekerjaanForm(forms.Form):
    pendidikantrkhr = forms.CharField(label='Pendidikan Terakhir', widget=forms.Select(choices=PT_SELECT))
    pekerjaan = forms.CharField(label='Pekerjaan', widget=forms.Select(choices=WORK_SELECT))
    industri = forms.CharField(label='Industri Pekerjaan', widget=forms.Select(choices=INDUSTRI_SELECT))
    pendapatan = forms.CharField(label='Pendapatan Per Bulan', widget=forms.Select(choices=PENDAPATAN_SELECT))
    sumber = forms.CharField(label='Sumber Pendapatan', widget=forms.Select(choices=SUMBER_SELECT))

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
class PreferensiForm(forms.Form):
    budgetinvestasi = forms.CharField(label='Budget Investasi', widget=forms.Select(choices=PENDAPATAN_SELECT))
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

    Investasi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)

class PreferensiInvestasi(forms.Form):
    OPTIONS = ( #JEKUHDEDB BARU SADAR KALO UMKM
        ("retail", "Retail"),
        ("otomotif", "Otomotif"),
        ("finansial", "Finansial")
    )

    PreferensiInvestasi = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)

class moform(forms.ModelForm):
    class Meta:
        model = EditProfil
        fields = '__all__'