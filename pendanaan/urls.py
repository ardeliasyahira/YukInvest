from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from .views import *

app_name = 'pendanaan'

urlpatterns = [
    path("", index, name="index"),
    path("api/", get_umkm, name="api_umkm"),
    path("api-view/", view_umkm_flutter, name="api_view"),
    path("api-global/", view_all_umkm_flutter, name="api_global"),
    path("api-add/", add_umkm_flutter, name="api_add"),
    path("add/", add_umkm, name="add_umkm"),
    path("view/", view_umkm, name="view_umkm")
]

