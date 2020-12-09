from django.contrib.auth.models import User
from django.db import models


class ProfilePic(models.Model):
    profile_picture = models.ImageField(upload_to='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

