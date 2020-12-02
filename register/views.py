from django.shortcuts import render

from register.forms import CreateUser


def register(request):
    if request.method == 'GET':
        form = CreateUser()
        context = {
            'form': form
        }
        return render(request, 'register/login.html', context)
