from django.urls import path
from . import views

app_name = 'profil'

urlpatterns = [
    # path('', views.investasi_view, name='Investasi'),
    # path('', views.accountSettings, name='Acc settings'),
    # path('', views.datadiri_form, name='Data Diri'),
    # path('', views.pekerjaan_form, name='Pekerjaan'),
    # path('', views.preferensi_form, name='Preferensi'),
    # path('edit_profil/', views.UserEdit, name='edit_profile')
    path('', views.datadiri_form, name = '')
]