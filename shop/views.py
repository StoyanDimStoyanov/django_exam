from django.contrib.auth.models import User
from django.shortcuts import render

from shop.forms import CreateAnnounceForm
from shop.models import Announcement


def index(request):

    context = {
        "user": request.user.is_authenticated,
    }
    return render(request, 'index.html', context)


def search(request):
    items = Announcement.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'search_results.html', context)


def create_announce(request):
    if request.method == "GET":
        form = CreateAnnounceForm
        context = {
            "form": form
        }
        return render(request, )