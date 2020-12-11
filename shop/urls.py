
from django.urls import path

from shop.views import index, search, create_announce, edit_announcement, announce_details, delete_announce

urlpatterns = [
                  path('', index, name='index page'),
                  path('results/', search, name='result page'),
                  path('create_announce/', create_announce, name='create announcement'),
                  path('edit_announce/<int:pk>', edit_announcement, name='edit announce'),
                  path('details_announce/<int:pk>', announce_details, name='details  announce'),
                  path('delete_announce/<int:pk>', delete_announce, name='delete  announce'),
              ]
