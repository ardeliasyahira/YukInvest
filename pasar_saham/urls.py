from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<str:pk>/', detail, name='detailsaham'),
]
