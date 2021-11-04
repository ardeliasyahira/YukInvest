from django.shortcuts import render
from pendanaan.models import UMKM
from django.template.loader import render_to_string
from django.http import JsonResponse


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

