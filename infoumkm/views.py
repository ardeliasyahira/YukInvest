from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.core import serializers
from pendanaan.models import UMKM
from .forms import UmkmForm

# Create your views here.
def daftarumkm(request):
    umkms = UMKM.objects.all().values()
    response = {'umkms': umkms}
    return render(request, 'daftarumkm.html', response)

def daftarumkm_detail(request, slug):
  umkms = get_object_or_404(UMKM, slug=slug)
  response = {'umkms': umkms}
  return render(request, "daftarumkm_detail.html", response)

def daftarumkm_detail_popup(request, slug):
  umkms = get_object_or_404(UMKM, slug=slug)
  response = {'umkms': umkms}
  return render(request, "daftarumkm_detail_popup.html", response)

def add_umkm(request):
    form = UmkmForm()
    if request.method == 'POST':
        form = UmkmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/daftarumkm/')
        
    context = {'form':form}
    return render(request, 'info_form.html', context)