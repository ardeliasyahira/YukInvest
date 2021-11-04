from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from .views import *

app_name = 'pendanaan'

urlpatterns = [
    path("", index, name="index"),
    path("api/", get_umkm, name="api_umkm"),
    path("add/", add_umkm, name="add_umkm"),
    path("view/", view_umkm, name="view_umkm"),
    path("delete/<str:umkm_id>", delete_umkm, name="delete_umkm"),
]

# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)