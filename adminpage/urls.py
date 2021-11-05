from django.urls import path
from .views import *

app_name = "admin-page"

urlpatterns = [
    path("", index, name="index"),
    path("users-db/", user_index, name="user_index"),
    path("umkm-api/", get_umkm, name="api_umkm"),
    path("user-api/", get_user, name="api_user"),
    path("validate/<str:umkm_id>", validate_umkm, name="validate_umkm"),
    path("invalidate/<str:umkm_id>", invalidate_umkm, name="invalidate_umkm"),
    path("delete-umkm/<str:umkm_id>", delete_umkm, name="delete_umkm"),
    path("delete-user/<str:umkm_id>", delete_user, name="delete_user"),

]
