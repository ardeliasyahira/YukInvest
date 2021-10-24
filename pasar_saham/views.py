from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from pendanaan.models import UMKM


# Create your views here.
def index(request):
    notes = UMKM.objects.all()
    response = {'umkm': UMKM}
    return render(request, 'index.html', response)

class IndexView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return UMKM.objects.all()

class DetailView(generic.DetailView):
    model = UMKM
    template_name = 'detail.html'