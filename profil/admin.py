from django.contrib import admin
# from .models import EditProfil
from profil.forms import moform
from profil import models
# Register your models here.

class LeaveAdmin(admin.ModelAdmin):
    form = moform

admin.site.register(models.EditProfil, LeaveAdmin)
