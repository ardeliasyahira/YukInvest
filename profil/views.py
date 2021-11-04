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

# @login_required
# def my_view(request):
    
#     message = 'Unggah foto'
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = moform(docfile=request.FILES['docfile'])
#             newdoc.save()
#             # Redirect to the document list after POST
#             return redirect('my-view')
#         else:
#             message = 'The form is not valid. Fix the following error:'
#     else:
#         form = moform()  # An empty, unbound form

#     # Load documents for the list page
#     documents = EditProfil.objects.all()

#     # Render list page with the documents and the form
#     context = {'documents': documents, 'form': form, 'message': message}
#     return render(request, 'bbbootstrap-snippet.html', context)

# @login_required
# def investasi_view(request):
#     if request.method == 'POST':
#         form = InvestasiForm(request.POST)
#         if form.is_valid():
#             countries = form.cleaned_data.get('investasi')
#             # do something with your results
#     else:
#         form = InvestasiForm

#     return render_to_response('bbbootstrap-snippet.html', {'form': form},
#                               context_instance=RequestContext(request))

# @login_required
# def accountSettings(request):
#     context = {}
#     return render(request, 'bbbootstrap-snippet.html', context)


# @login_required
# class EmpImageDisplay(DetailView):
#     model = EditProfil
#     template_name = 'bbbootstrap-snippet.html'
#     context_object_name = 'avatar'

@login_required
def datadiri_form(request):
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = DataDiriForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return redirect('/profil/')

    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = DataDiriForm()
    
    # response ={
    #     'form':form
    # }
    # return render(request, 'bbbootstrap-snippet.html',response)
    if request.method == 'POST':
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
    else:
        editprofil = EditProfil.objects.all()
        context = {
            'editprofil': editprofil
        }

    return render(request, 'bbbootstrap-snippet.html', context)

    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = PekerjaanForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return redirect('/profil/')

    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = PekerjaanForm()
    
    # response ={
    #     'form':form
    # }
    # return render(request, 'Edit_profile_page.html',response)
    # form = PekerjaanForm()

    # if request.method == "POST":
    #     form  = PekerjaanForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # obj.author = request.user
    #         return HttpResponseRedirect('bbbootstrap-snippet.html')

    # response = {'form': form}
    # return render(request, 'bbbootstrap-snippet.html', response)

# @login_required
# def preferensi_form(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         print(request.POST)
#         # create a form instance and populate it with data from the request:
#         form = PreferensiForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return redirect('/profil/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = PreferensiForm()
    
#     response ={
#         'form':form
#     }
#     return render(request, 'bbbootstrap-snippet.html',response)


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



