from django.shortcuts import redirect, render
from .models import EditProfil
from .forms import DocumentForm, InvestasiForm, PreferensiInvestasi


def my_view(request):
    print(f"Berhasil di upload")
    message = 'Unggah foto'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = EditProfil(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = EditProfil.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)

def investasi_view(request):
    if request.method == 'POST':
        form = InvestasiForm(request.POST)
        if form.is_valid():
            countries = form.cleaned_data.get('investasi')
            # do something with your results
    else:
        form = InvestasiForm

    return render_to_response('multiple.html', {'form': form},
                              context_instance=RequestContext(request))

def prefinvestasi_view(request):
    if request.method == 'POST':
        form = PreferensiInvestasi(request.POST)
        if form.is_valid():
            countries = form.cleaned_data.get('investasi')
            # do something with your results
    else:
        form = PreferensiInvestasi

    return render_to_response('multiple.html', {'form': form},
                              context_instance=RequestContext(request))