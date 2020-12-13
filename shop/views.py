import os
from os.path import join

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from examProject.settings import BASE_DIR
from shop.forms import CreateAnnounceForm
from shop.models import Announcement


def index(request):
    if request.method == "GET":
        if "term" in request.GET:
            search_result = Announcement.objects.filter(name__icontains=request.GET.get('term'))
            names = [x.name for x in search_result]
            return JsonResponse(names, safe=False)
        context = {
            "authenticated": request.user.is_authenticated,
            'anonymous': request.user.is_anonymous,
            'all_announce': Announcement.objects.all(),
        }
        return render(request, 'index.html', context)
    search_for = request.POST.get('search_bar')
    result = Announcement.objects.filter(name__icontains=search_for)
    context = {
        'results': result,
    }
    return render(request, 'search_results.html', context)


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


@login_required
def edit_announcement(request, pk):

    announce = Announcement.objects.get(pk=pk)
    if announce.seller_id != request.user.id:
        return HttpResponse("<h1 style='font-size: 3.4rem'>You are not allowed to edit somebody's else announce</h1>")
    if request.method == "GET":

        form = CreateAnnounceForm(instance=announce)
        context = {
            'form': form,
            'pk': pk,
        }
        return render(request, 'edit_announce.html', context)
    form = CreateAnnounceForm(request.POST, request.FILES, instance=announce)
    if form.is_valid():
        existing_pic = Announcement.objects.get(pk=pk)
        if existing_pic.seller_id == request.user.id and\
                existing_pic.image.url != f" media/image/{request.FILES.get('image')}" \
                and len(request.FILES) > 0:
            os.remove(f'media/{existing_pic.image}')
        form.save()
        return redirect('user profile', request.user.id)
    context = {
        'form': form,
    }
    return render(request, 'edit_announce.html', context)


@login_required
def announce_details(request, pk):
    announce = Announcement.objects.get(pk=pk)
    user = User.objects.get(pk=announce.seller_id)
    can_delete = False
    if request.user.id == user.id:
        can_delete = True
    context = {
        'announce': announce,
        'user':user,
        'can_delete': can_delete
    }
    return render(request, 'announce_details.html', context)


@login_required
def delete_announce(request, pk):
    announce = Announcement.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'announce': announce,
        }
        return render(request, 'delete_announce.html', context)
    pic_to_delete = announce.image.url
    print(os.path.join(BASE_DIR, pic_to_delete))
    os.remove(f'media/{announce.image}')
    announce.delete()

    return redirect('user profile', request.user.id)
