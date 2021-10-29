from django.urls import path
from .views import *

app_name = 'pendanaan'

urlpatterns = [
    path("", index, name="index"),
    path("api/", get_umkm, name="api_umkm"),
    path("add/", add_umkm, name="add_umkm"),
    path("delete/<str:umkm_id>", delete_umkm, name="delete_umkm"),
]