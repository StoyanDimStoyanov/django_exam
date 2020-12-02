from django.shortcuts import render

from shop.models import Announcement


def index(request):
    return render(request, 'index.html')


def search(request):
    items = Announcement.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'search_results.html', context)