from django.contrib.auth.models import User
from django.db import models


class Announcement(models.Model):
    NEW = 'Ново'
    USED = 'Употребявано'
    CONDITION_TYPES = ((NEW, 'Ново'), (USED, 'Употрябавано'))

    name = models.CharField(blank=False, max_length=30)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images')
    condition = models.CharField(max_length=12, choices=CONDITION_TYPES, default='Unknown')
    price = models.IntegerField(null=False)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30)


