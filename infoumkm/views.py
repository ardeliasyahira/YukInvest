from django.shortcuts import render
from django.http.response import HttpResponse
from django.core import serializers
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'info.html')