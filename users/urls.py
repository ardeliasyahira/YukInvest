# from django.urls import path, include

# from .views import user_login, user_logout, user_register

# urlpatterns = [
#     path('login', user_login, name = 'login'),
#     path('logout', user_logout, name = 'logout'),
#     path('register', user_register, name = 'register'),
# ]

# app_name = 'users'

from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', signin, name="login"),
    path('register/', signup, name="register"),
    path('signout/', signout, name="signout"),
    path('loginflutter', loginFlutter, name='loginFlutter'),
    path('registerflutter', registerFlutter, name='registerFlutter'),
    path('logoutflutter',logoutFlutter,name='logoutFlutter'),
]

