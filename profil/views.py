from django.shortcuts import redirect, render
from .models import EditProfil
from .forms import moform
from django.views.generic import DetailView
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from astroid import context
from urllib3.util import request
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.utils.datastructures import MultiValueDictKeyError

@login_required
def datadiri_form(request):
    if request.method == 'POST':
        form = moform(request.POST or None, request.FILES or None)
        namadepan = request.POST.get('namadepan')
        namabelakang = request.POST.get('namabelakang')
        deskripsibisnis = request.POST.get('deskripsibisnis')
        deskripsisumber = request.POST.get('deskripsisumber')
        sid = request.POST.get('sid')
        noktp = request.POST.get('noktp')
        obj = EditProfil.objects.create(
            namadepan=namadepan, namabelakang=namabelakang, deskripsibisnis=deskripsibisnis, deskripsisumber=deskripsisumber, sid=sid, noktp=noktp)
        if obj:
            return redirect('/')
        return HttpResponse("")
        # if form.is_valid():
        # # save the form data to model
        #     form.save()
        # return HttpResponseRedirect('/')
    else:
        editprofil = EditProfil.objects.all()
        context = {
            'editprofil': editprofil
        }

    return render(request, 'bbbootstrap-snippet.html', context)

class UserEdit(generic.UpdateView):
    form_class = moform
    template_name = 'bbbootstrap-snippet.html'
    success_url = reverse_lazy('homepage')

    def get_object(self):
        return self.request.user

def model_list(request):
    profil = EditProfil.objects.all() # Mengambil seluruh Note yang ada di database
    response = {'edit': edit} #notes: query set (list berisi model) --> bakal dimasukkan ke lab_2.html
    return render(request, 'bbbootstrap-snippet.html', response)



