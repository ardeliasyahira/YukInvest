from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.http import JsonResponse
from pendanaan.models import UMKM
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q
from .forms import SearchForm


# Create your views here.
def index(request):
    url_param = request.GET.get("q")

    if url_param:
        umkms = UMKM.objects.filter(merek_bisnis__icontains=url_param)
    else:
        umkms = UMKM.objects.all()

    if request.is_ajax():
        html = render_to_string(
            template_name="search.html", context={"umkm": umkms}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    response = {'umkm': umkms}
    return render(request, 'index.html', response)


def detail(request, pk):
    umkm = UMKM.objects.get(merek_bisnis=pk)
    return render(request, 'detail.html', {'detail_umkm': umkm})

# def search(request):
#     if 'search' in request.GET:
#         value = request.GET['search']
#         umkm = UMKM.objects.filter(merek_usaha__startswith=value)
#     else:
#         umkm = UMKM.objects.all()
#
#     html = render_to_string(template_name='index.html', context={'umkm': umkm})
#     value_dict = {'html_from_view': html}
#     return JsonResponse(data=value_dict, safe=False)


def search(request):
    searched = request.POST['searched']
    umkm = UMKM.objects.filter(Q(merek_usaha__contains=searched) | Q(domisili__contains=searched)).order_by('merek_usaha')

    if request.method == "POST":
        return render(request, 'search.html', {'searched': searched, 'umkm': umkm})
    else:
        return render(request, 'search.html', {})
