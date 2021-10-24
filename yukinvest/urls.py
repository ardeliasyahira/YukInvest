"""yukinvest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import homepage.urls as homepage
import pasar_saham.urls as pasar_saham
import pendanaan.urls as pendanaan
import infoumkm.urls as infoumkm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(homepage)),
    path('pendanaan/', include(pendanaan)),
# <<<<<<< HEAD
    path('pasarsaham/', include(pasar_saham)),
# =======
    path('info/', include(infoumkm)),
# >>>>>>> d80c8fcd999f5f4274f82dc6c48381cc3db6d6d8
]
