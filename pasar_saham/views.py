from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.http import JsonResponse
from django.views.generic import ListView
from pendanaan.models import UMKM
from django.template.loader import render_to_string
from django.http import JsonResponse
from .forms import SearchForm


# Create your views here.
def index(request):
    umkms = UMKM.objects.all()
    response = {'umkm': umkms}
    return render(request, 'index.html', response)


def detail(request, pk):
    umkm = UMKM.objects.get(merek_bisnis=pk)
    return render(request, 'detail.html', {'detail_umkm': umkm})

# def search(request):
#     # request.POST : string isi form ; request.FILES :
#     if 'search' in request.GET:
#         value = request.GET['search']
#         umkm = UMKM.objects.filter(merek_usaha__startswith=value)
#     else:
#         umkm = UMKM.objects.all()
#
#     html = render_to_string(template_name='index.html', context={'umkm': umkm})
#     print(umkm)
#     value_dict = {'html_from_view': html}
#     return JsonResponse(data=value_dict, safe=False)

def search_keyword_all(request):

    if (request.method == "POST"):
        return redirect('umkm:search_keyword_all')

    items = UMKM.objects.all()
    context = {
        'Items': items,
        'queryResult': 'Menampilkan semua barang '
    }

    return render(request, 'index.html', context)

def search_keyword(request, keyword):

    if (request.method == "POST" and request.POST['keyword'] == ''):
        return redirect('umkm:search_keyword_all')

    if (request.method == "POST"):
        return redirect('umkm:search_keyword', keyword = request.POST['keyword'])

    items = UMKM.objects.all()
    items = [i for i in UMKM.objects.all() if (keyword in "".join(i.nama.split()).lower())]
    context = {
        'Items': items,
        'queryResult': 'barang dengan kata kunci ' + keyword
    }

    return render(request, 'index.html', context)




# if request.is_valid():
#     search_qs = UMKM.objects.filter(merek_usaha__startswith=value)
#
# return render(request, "detail.html", {'detail_umkm': search_qs})

# class SearchView(ListView):
#     model = UMKM
#     template_name = 'search.html'
#     context_object_name = 'all_search_results'
#
#     def get_queryset(self):
#        result = super(SearchView, self).get_queryset()
#        query = self.request.GET.get('search')
#        if query:
#           postresult = Article.objects.filter(title__contains=query)
#           result = postresult
#        else:
#            result = None
#        return result

#
# def search(request):
#     if request.method=='POST':
#         form = SearchForm(request.POST)
#
#         search_input = json.loads(request.body).get('searchText')
#
#         input = UMKM.filter(merek_bisnis__starts__with=search_input) | UMKM.filter(produk_jasa__starts__with=search_input)|\
#                 UMKM.filter(domisili__starts__with=search_input)
#
#         data = input.values()
#
#         return JsonResponse(list(data), safe=False)

# class InfoListView(ListView):
#     model = UMKM
#     template_name = 'index.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["qs_json"] = json.dumps(list(UMKM.objects.values()))
