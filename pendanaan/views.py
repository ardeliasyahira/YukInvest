from typing import final
from django.shortcuts import redirect, render
from pendanaan.forms import UMKMForm
from .models import UMKM
from django.core import serializers
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "pendanaan/index_pendanaan.html")

@login_required(login_url="users:login")
def view_umkm(request):
    obj = UMKM.objects.filter(request.user).get(pk=1)
    obj_dict = {"obj": obj}
    return render(request, "pendanaan/view_umkm.html", obj_dict)

@login_required(login_url="users:login")
def get_umkm(request):
    umkm = UMKM.objects.filter(request.user).get(pk=1)
    umkm_json = serializers.serialize("json", umkm)
    return HttpResponse(umkm_json, content_type="application/json")

@login_required(login_url="users:login")
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