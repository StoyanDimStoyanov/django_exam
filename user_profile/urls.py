from django.urls import path

from user_profile.views import user_profile, change_profile_pic

urlpatterns = [
    path('<int:pk>', user_profile, name='user profile'),
    path('changeprofilepic/', change_profile_pic, name='change profile pic'),

]
