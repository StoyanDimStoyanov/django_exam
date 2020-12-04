from django.urls import path

from accounts.views import register, log_out_user, login_view

urlpatterns = [
    path('', register, name='create profile'),
    path('login/', login_view, name='log in'),
    path('logout/', log_out_user, name='log out')
]
