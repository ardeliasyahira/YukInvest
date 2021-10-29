from django.urls import path
from django.conf.urls import url
from .views import index, detail, search_keyword, search_keyword_all

urlpatterns = [
    path('', index, name='index'),
    path('<str:pk>/', detail, name='detailsaham'),
    # path('search', index, name='search'),
    path('search/keyword/<str:keyword>/', search_keyword, name='search_keyword'),
    path('search/keyword/', search_keyword_all, name='search_keyword_all'),
]
