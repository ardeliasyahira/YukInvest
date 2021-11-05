from django.urls import path
from .views import index, detailsaham, edit_feedback, delete_feedback

app_name = 'homepage'
urlpatterns = [
    path('', index, name='index'),
    path('edit_feedback', edit_feedback, name='edit_feedback'),
    path('delete_feedback', delete_feedback, name='delete_feedback'),
    path('detailsaham/', detailsaham, name='detailsaham')
]