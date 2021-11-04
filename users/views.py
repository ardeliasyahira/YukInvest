from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 

from .forms import AuthForm

# Create your views here.
def user_login(request):
    # if (not request.user.is_anonymous):
	#     return redirect(resolve_url('/'))

    form = AuthForm(request.POST or None)
    context = {
        'form': form,
        'isError': False,
        'Error': '',
    }

    if (request.method == "POST"):
        account = authenticate(
            username = request.POST['nama'],
            password = request.POST['password'],
        )

        if (account == None):
            context['isError'] = True
            context['Error'] = 'Autentikasi gagal'
            context['form'] = AuthForm()
            return render(request, 'login.html', context)
        else:
            login(request, account)
            return redirect(resolve_url('/'))

    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect(resolve_url('users:login'))
