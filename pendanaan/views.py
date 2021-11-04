from typing import final
from django.shortcuts import redirect, render
from pendanaan.forms import UMKMForm
from .models import UMKM
from django.core import serializers
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "pendanaan/index_pendanaan.html")

# @login_required(login_url="")
def view_umkm(request):
    return render(request, "pendanaan/view_umkm.html")

# @login_required(login_url="")
def get_umkm(request):
    umkm = UMKM.objects.all()
    umkm_json = serializers.serialize("json", umkm)
    return HttpResponse(umkm_json, content_type="application/json")

# @login_required(login_url="")
def add_umkm(request):
    form = UMKMForm()
    if request.method == "POST":
        # data = request.POST.dict()
        # data["user"] = request.user
        form = UMKMForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pendanaan:view_umkm")
    context = {"form": form}
    return render(request, "pendanaan/add_umkm.html", context)


# @login_required(login_url="")
def delete_umkm(request, umkm_id):
    try:
        UMKM.objects.get(id=umkm_id).delete()
    except Exception as e:
        print(e)
    finally:
        return redirect("") #