from django.db import models

# Create your models here.

class EditProfil(models.Model):
    fotoprofil = models.FileField(upload_to='documents/%Y/%m/%d')
    namadepan = models.CharField(max_length=30)
    namabelakang = models.CharField(max_length=30)
    tempatlahir = models.CharField(max_length=30)
    tanggallahir = models.DateField()
    latarbelakang = models.TextField()
    notelpon = models.IntegerField()
    norumah = models.IntegerField()
    alamatktp = models.TextField()
    provinsi = models.CharField(max_length = 30)
    kotakabu = models.CharField(max_length = 30)
    kecamatan = models.CharField(max_length = 30)
    kelurahan = models.CharField(max_length = 30)
    rt = models.IntegerField()
    rw = models.IntegerField()
    alamatskrg = models.TextField()
    provinsi2 = models.CharField(max_length = 30)
    kotakabu2 = models.CharField(max_length = 30)
    kecamatan2 = models.CharField(max_length = 30)
    kelurahan2 = models.CharField(max_length = 30)
    rt2 = models.IntegerField()
    rw2 = models.IntegerField()
#Pekerjaan
    deskripsibisnis = models.TextField()
    deskripsisumber = models.TextField()
#Dokumen
    sid = models.IntegerField()
    noktp = models.IntegerField()
    fotoktp = models.FileField(upload_to='documents/%Y/%m/%d')
    fotoselfie = models.FileField(upload_to='documents/%Y/%m/%d')
#Bank
    namabank = models.CharField(max_length=50)
    norekening = models.IntegerField()
    namapemilik = models.CharField(max_length=50)
    namaibu = models.CharField(max_length=50)
    namaahliwaris = models.CharField(max_length=50)
    ubahliwaris = models.CharField(max_length=50)








