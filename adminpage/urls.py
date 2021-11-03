from django.urls import path
from .views import *

app_name = "admin-page"

urlpatterns = [
    path("", index, name="index"),
    path("users-db/", user_index, name="user_index"),
    path("umkm-api/", get_umkm, name="api_umkm"),
    path("user-api/", get_user, name="api_user"),
]
