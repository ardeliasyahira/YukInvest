from django.urls import path
from . import views

app_name = 'profil'

urlpatterns = [
    path('', views.my_view, name='My view'),
    path('', views.investasi_view, name='Investasi'),
    path('', views.accountSettings, name='Acc settings'),
    path('', views.datadiri_form, name='Data Diri'),
    path('', views.pekerjaan_form, name='Pekerjaan'),
    path('', views.preferensi_form, name='Preferensi')
]