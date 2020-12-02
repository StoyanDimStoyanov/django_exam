from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from shop.views import index, search

urlpatterns = [
    path('', index, name='index page'),
    path('results/', search, name='index page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
