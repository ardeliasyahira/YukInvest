# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect, resolve_url
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User 

# from .forms import AuthForm

# # Create your views here.
# def user_login(request):
#     # if (not request.user.is_anonymous):
# 	#     return redirect(resolve_url('/'))

#     form = AuthForm(request.POST or None)
#     context = {
#         'form': form,
#         'isError': False,
#         'Error': '',
#     }

#     if (request.method == "POST"):
#         account = authenticate(
#             username = request.POST['nama'],
#             password = request.POST['password'],
#         )

#         if (account == None):
#             context['isError'] = True
#             context['Error'] = 'Autentikasi gagal'
#             context['form'] = AuthForm()
#             return render(request, 'login.html', context)
#         else:
#             login(request, account)
#             return redirect(resolve_url('/'))

#     return render(request, 'login.html', context)

# def user_register(request):
#     if (not request.user.is_anonymous):
# 	    return redirect(resolve_url('/'))

#     form = AuthForm(request.POST or None)
#     context = {
#         'form': form,
#         'isError': False,
#         'Error': '',
#     }

#     if (request.method == "POST"):
#         acount = None
#         try:
#             account = User.objects.get(username = request.POST['nama'])
#         except:
#             account = None
#         if (account == None):
#             new_account = User.objects.create_user(request.POST['nama'], '', request.POST['password'])
#             new_account.save()
#             login(request, new_account)
#             return redirect(resolve_url('/'))
#         else:
#             context['isError'] = True
#             context['Error'] = 'Sudah ada akun dengan username ' + request.POST['nama']
#             context['Form'] = AuthForm()
#             return render(request, 'register.html', context)


#     return render(request, 'register.html', context)

# def user_logout(request):
#     logout(request)
#     return redirect(resolve_url('users:login'))

# INI CODE SEBELUM GANIII
# from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login, logout

# # Create your views here.

# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#         return render(request, "register.html")
#     else:
#         return render(request, "register.html")

# def login(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/")
#         return render(request, "login.html")
#     else:
#         return render(request, "login.html")

# def signout(request):
#     logout(request)
#     return redirect("/")



    # INI CODE GANIIIIIII
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
        return render(request, "register.html")
    else:
        return render(request, "register.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage:index")
        return render(request, "login.html")
    else:
        return render(request, "login.html")

def signout(request):
  logout(request)
  return redirect("/")

