from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import join


class Announcement(models.Model):
    NEW = 'Ново'
    USED = 'Употребявано'
    CONDITION_TYPES = ((NEW, 'Ново'), (USED, 'Употрябавано'))
    WORK = "Работа"
    ELECTRONICS = 'Електроника'
    CARS = 'Коли'
    CLOTHES = 'Дрехи'
    HOME = 'За дома'
    GiFTS = 'Подаръци'
    ALL = 'Всички'
    CATEGORIES_CHOICES = (
        (WORK, 'Работа'),
        (ELECTRONICS, 'Електроника'),
        (CARS, 'Коли'),
        (CLOTHES, 'Дрехи'),
        (HOME, 'За дома'),
        (GiFTS, 'Подаръци'),
        (ALL, 'Всички')
    )

    name = models.CharField(blank=False, max_length=30)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images')
    condition = models.CharField(max_length=12, choices=CONDITION_TYPES, default='Unknown')
    price = models.IntegerField(null=False)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=30, choices=CATEGORIES_CHOICES, default='Всички')

    def __str__(self):
        return ", ".join([self.name, f'Published on: {str(self.date_published)[:10]}'])
