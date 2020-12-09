from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from shop.views import index, search, create_announce

urlpatterns = [
    path('', index, name='index page'),
    path('results/', search, name='result page'),
    path('create_announce/', create_announce, name='create announcement'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
