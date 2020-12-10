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
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
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
        return render(request, 'accounts/login.html', context)
    form = LogInForm(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        context = {
            'authenticated': True,
        }
        # if len(request.POST.get('next')) > 0 and request.POST.get('next'):
        #     return redirect(request.POST.get('next'))
        return render(request, 'index.html', context)
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def log_out_user(request):
    logout(request)
    return redirect('index page')

