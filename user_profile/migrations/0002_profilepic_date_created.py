# Generated by Django 3.1.3 on 2020-12-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepic',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]