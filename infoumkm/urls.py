from django.urls import path
from django.conf.urls import url
from .views import add_umkm, daftarumkm, daftarumkm_detail, daftarumkm_detail_popup

urlpatterns = [
    path('', daftarumkm, name='daftarumkm'),
]