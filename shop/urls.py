
from django.urls import path

from shop.views import index, search, create_announce, edit_announcement

urlpatterns = [
                  path('', index, name='index page'),
                  path('results/', search, name='result page'),
                  path('create_announce/', create_announce, name='create announcement'),
                  path('edit_announce/<int:pk>', edit_announcement, name='edit announce'),
              ]
