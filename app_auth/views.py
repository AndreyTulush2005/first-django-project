from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def profile_view(requests):
    return render(request=requests, template_name="app_auth/profile.html")


def login_view(requests):
    redirect_url = reverse('profile')
    if requests.method == "GET":
        if requests.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request=requests, template_name="app_auth/login.html")
    else:
        username = requests.POST['username']
        password = requests.POST['password']
        user = authenticate(requests, username=username, password=password)
        if user is not None:
            login(requests, user)
            return redirect(redirect_url)
        else:
            return render(request=requests, template_name="app_auth/login.html", context={'error' : "Пользователь не найден!"})


def register_view(requests):
    return render(request=requests, template_name='app_auth/register.html')


def logout_view(requests):
    logout(requests)
    return redirect(reverse('login'))