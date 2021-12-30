import json

from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, UserModel
from .forms import AuthForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, "login.html")
    

def signout(request):
  logout(request)
  return redirect("users:login")

@csrf_exempt
def registerFlutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        username = data["username"]
        password1 = data["password1"]

        newUser = UserModel.objects.create_user(
        username = username, 
        password = password1,
        )

        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def loginFlutter(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "username": request.user.username,
              "message": "Successfully Logged In!"
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def logoutFlutter(request):
    try:
        logout(request)
        return JsonResponse({
                    "status": True,
                    "message": "Successfully Logged out!"
                }, status=200)
    except:
        return JsonResponse({
          "status": False,
          "message": "Failed to Logout"
        }, status=401)

