from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class EditProfil(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default='') # Delete profile when user is deleted
    namauser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="namauser", null = True, blank = True)
    namadepan = models.CharField(max_length = 30, default = '', null = True)
    namabelakang = models.CharField(max_length = 30, default = '', null = True)
#Pekerjaan
    deskripsibisnis = models.TextField(default = '', null = True)
    deskripsisumber = models.TextField(default = '', null = True)
#Dokumen
    sid = models.IntegerField(default = '', null = True)
    noktp = models.IntegerField(default = '',null = True)
#Bank
    namabank = models.CharField(max_length=50, default = '', null = True)
    norekening = models.IntegerField(null = True)
    namapemilik = models.CharField(max_length=50, default = '', null = True)
#Preferensi








