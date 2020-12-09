from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from shop.forms import CreateAnnounceForm
from shop.models import Announcement


def index(request):
    context = {
        "authenticated": request.user.is_authenticated,
        'anonymous': request.user.is_anonymous
    }
    return render(request, 'index.html', context)


def search(request):
    items = Announcement.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'search_results.html', context)


@login_required
def create_announce(request):
    if request.method == "GET":
        form = CreateAnnounceForm
        context = {
            "form": form,
            # 'authenticated': request.user.is_authenticated,
            'title': 'Качи обява',
        }
        return render(request, 'make_announcement.html', context)
    form = CreateAnnounceForm(request.POST, request.FILES)

    if form.is_valid():
        announcement = Announcement()
        announcement.name = form.cleaned_data['name']
        announcement.seller_id = request.user.id
        announcement.description = form.cleaned_data['description']
        announcement.image = request.FILES.get('image')
        announcement.condition = form.cleaned_data['condition']
        announcement.price = form.cleaned_data['price']
        announcement.category = form.cleaned_data['category']
        announcement.save()

        announcement.save()
        return redirect('user profile', request.user.id)
    context = {
        'form': form,
    }
    return render(request, 'make_announcement.html', context)
