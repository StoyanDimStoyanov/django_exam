from django import forms
from django.contrib.auth.models import User


class CreateUser(forms.ModelForm):
    class Meta():
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            model = User
        fields = ['first_name', 'last_name', 'password', 'username', 'email']
        for item in fields:
            self.fields['name'].widget.attrs.update({'class': 'special'})