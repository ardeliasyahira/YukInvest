from django.shortcuts import redirect, render
from .models import EditProfil
from .forms import DocumentForm, InvestasiForm, moform, DataDiriForm, PekerjaanForm, PreferensiForm
from django.views.generic import DetailView


def my_view(request):
    message = 'Unggah foto'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = moform(docfile=request.FILES['docfile'])
            newdoc.save()
            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = moform()  # An empty, unbound form

    # Load documents for the list page
    documents = EditProfil.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'Edit_profile_page.html', context)

def investasi_view(request):
    if request.method == 'POST':
        form = InvestasiForm(request.POST)
        if form.is_valid():
            countries = form.cleaned_data.get('investasi')
            # do something with your results
    else:
        form = InvestasiForm

    return render_to_response('Edit_profile_page.html', {'form': form},
                              context_instance=RequestContext(request))


def accountSettings(request):
    context = {}
    return render(request, 'Edit_profil_page.html', context)



class EmpImageDisplay(DetailView):
    model = EditProfil
    template_name = 'Edit_profile_page.html'
    context_object_name = 'avatar'

def datadiri_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DataDiriForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('/profil/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DataDiriForm()
    
    response ={
        'form':form
    }
    return render(request, 'Edit_profile_page.html',response)

def pekerjaan_form(request):
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
    from .forms import PekerjaanForm
    pekerjaan_form = PekerjaanForm()
    return render(request, 'Edit_profile_page.html', locals())

def preferensi_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PreferensiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('/profil/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PreferensiForm()
    
    response ={
        'form':form
    }
    return render(request, 'Edit_profile_page.html',response)





