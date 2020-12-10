from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
import os

from shop.forms import CreateAnnounceForm
from shop.models import Announcement
from user_profile.forms import ChangeProfilePic
from user_profile.models import ProfilePic


@login_required
def user_profile(request, pk):
    if request.user.id == pk:
        if request.method == 'GET':

            try:
                context = {
                    'profile_picture': ProfilePic.objects.get(user_id=pk),
                    'announces': Announcement.objects.filter(seller_id=pk)
                }
            except:
                context = {
                    'profile_picture': None,
                    'announces': Announcement.objects.filter(seller_id=pk)
                }
            return render(request, 'profile/user_profile.html', context)
    else:
        return HttpResponse("<h1 style='font-size: 3.4rem'>You are not allowed to view this page</h1>")


@login_required
def change_profile_pic(request):
    if request.method == 'GET':
        form = ChangeProfilePic
        context = {
            'form': form,
        }
        return render(request, 'profile/change_user_pic.html', context)
    form = ChangeProfilePic(request.method, request.FILES)
    if form.is_valid():
        try:
            existing_pic = ProfilePic.objects.get(user_id=request.user.id)
            os.remove(f'media/{existing_pic.profile_picture}')
            existing_pic.delete()
        except:
            pass
        table = ProfilePic()
        table.profile_picture = request.FILES.get('profile_picture')
        table.user = request.user
        table.save()

        return redirect('user profile', request.user.id)
    context = {
        'form': form,
    }
    return render(request, 'profile/change_user_pic.html', context)


