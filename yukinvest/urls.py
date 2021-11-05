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
from django.conf import settings
from django.conf.urls.static import static
import homepage.urls as homepage
import pendanaan.urls as pendanaan
import profil.urls as profil
import infoumkm.urls as infoumkm
import adminpage.urls as adminpage
import users.urls as users
import pasar_saham.urls as pasarsaham

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(homepage)),
    path('pendanaan/', include(pendanaan)),
    path('info/', include(infoumkm)),
    path('profil/', include(profil)),
    path('adminpage/', include(adminpage)),
    path('daftarumkm/', include(infoumkm)),
    path('users/', include(users)),
    path('daftarumkm/', include(infoumkm)),
    path('pasarsaham/', include(pasarsaham)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
