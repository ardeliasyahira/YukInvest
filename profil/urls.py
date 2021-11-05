from django.urls import path
from .views import my_view

app_name = 'profil'

urlpatterns = [
    path('', my_view, name='my-view')
]