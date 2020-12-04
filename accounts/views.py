from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import CreateUser, LogInForm


def register(request):
    if request.method == 'GET':
        form = CreateUser()
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)
    else:
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.username, password=form.password1)
            return render(request, 'index.html')
        context = {
            'form': form,
        }
        return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == 'GET':
        form = LogInForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/LogIn.html', context)
    form = LogInForm(request)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index page')


def log_out_user(request):
    logout(request)
    return redirect('index page')

