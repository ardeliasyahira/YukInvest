from django.shortcuts import render, redirect
from pendanaan.models import UMKM
from profil.models import EditProfil

from django.core import serializers
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    return render(request, "umkmpage/umkm_list.html")

def user_index(request):
    return render(request, "userdbpage/user_db_list.html")

def get_umkm(request):
    umkms = UMKM.objects.all()
    umkm_json = serializers.serialize("json", umkms)
    return HttpResponse(umkm_json, content_type="application/json")

def get_user(request):
    user_db = EditProfil.objects.all()
    userdb_json = serializers.serialize("json", user_db)
    return HttpResponse(userdb_json, content_type="application/json")

def validate_umkm(request, umkm_id):
    return

def invalidate_umkm(request, umkm_id):
    return

def delete_user(request, user_id):
    return

def edit_user(request, user_id):
    return