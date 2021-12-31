from typing import final
from django.shortcuts import redirect, render
from pendanaan.forms import UMKMForm
from .models import UMKM
from django.core import serializers
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, "pendanaan/index_pendanaan.html")

# @login_required(login_url="users:login")
def view_umkm(request):
    obj = UMKM.objects.filter(request.user).get(pk=1)
    obj_dict = {"obj": obj}
    return render(request, "pendanaan/view_umkm.html", obj_dict)

# @login_required(login_url="users:login")
def get_umkm(request):
    umkm = UMKM.objects.filter(request.user).get(pk=1)
    umkm_json = serializers.serialize("json", umkm)
    return HttpResponse(umkm_json, content_type="application/json")

# @login_required(login_url="users:login")
def add_umkm(request):
    form = UMKMForm()
    umkm = UMKM.objects.filter(request.user).get(pk=1)
    if umkm:
        return redirect("pendanaan:view_umkm")
    elif request.method == "POST":
        data = request.POST.dict()
        data["user"] = request.user
        form = UMKMForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pendanaan:view_umkm")
    context = {"form": form}
    return render(request, "pendanaan/add_umkm.html", context)

# @login_required(login_url='/login/')
def view_umkm_flutter(request):
    form_umkm = UMKMForm(request.POST or None)

    if request.method == "GET":
        umkm = UMKM.objects.filter(user=request.user)
        data = serializers.serialize("json", umkm)
        return HttpResponse(data, content_type="application/json")

    if request.method == "POST" and form_umkm.is_valid():
        form = form_umkm.save(commit=False)
        form.user = request.user
        form.save()
        
        umkm = UMKM.objects.filter(user=request.user).last()
        return JsonResponse({'user': str(request.user), 'nama': umkm.nama, 'deskripsi':umkm.deskripsi, 'logo_usaha': logo_usaha})
    
    return JsonResponse({'nama': "", 'deskripsi':"", 'logo_usaha': ""})

def view_all_umkm_flutter(request):
    form_umkm = UMKMForm(request.POST or None)

    if request.method == "GET":
        umkm = UMKM.objects.all()
        data = serializers.serialize("json", umkm)
        return HttpResponse(data, content_type="application/json")

    if request.method == "POST" and form_umkm.is_valid():
        form = form_umkm.save(commit=False)
        form.user = request.user
        form.save()
        
        umkm = UMKM.objects.all()
        return JsonResponse({'user': str(request.user), 'nama': kegiatan.nama, 'deskripsi':kegiatan.deskripsi})
    
    return JsonResponse({'nama': "", 'deskripsi':""})

@csrf_exempt
def add_umkm_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nama = data["nama"]
        merek_bisnis  = data["merek_bisnis"]
        domisili = data["domisili"]
        produk_jasa = data["produk_jasa"]
        saham_umkm = data["saham_umkm"]
        pendanaan_dibutuhkan = data["pendanaan_dibutuhkan"]
        deskripsi = data["deskripsi"]
        logo_usaha = data["logo_usaha"]
	gambar_usaha = data["gambar_usaha"]
        ringkasan_perusahaan = data["ringkasan_perusahaan"]
        status = data["status"]

        form = UMKM(
            user = request.user,
            nama = nama,
            deskripsi = deskripsi,
            nama = nama,
            merek_bisnis  = merek_bisnis,
            domisili = domisili,
            produk_jasa = produk_jasa,
            saham_umkm = saham_umkm,
            pendanaan_dibutuhkan = pendanaan_dibutuhkan,
            deskripsi = deskripsi,
            logo_usaha = logo_usaha,
	    gambar_usaha = gambar_usaha,
            ringkasan_perusahaan = ringkasan_perusahaan,
            status = status
        )
        
        form.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)