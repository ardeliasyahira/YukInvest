# from django.urls import path, include

# from .views import user_login, user_logout, user_register

# urlpatterns = [
#     path('login', user_login, name = 'login'),
#     path('logout', user_logout, name = 'logout'),
#     path('register', user_register, name = 'register'),
# ]

# app_name = 'users'

from django.urls import path
from .views import signup, signin, signout

app_name = 'users'

urlpatterns = [
    path('login/', signin, name="login"),
    path('register/', signup, name="register"),
    path('signout/', signout, name="signout")
]

