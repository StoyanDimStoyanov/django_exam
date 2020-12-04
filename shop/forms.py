from django import forms

from shop.models import Announcement


class CreateAnnounceForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'

    def __init__(self):
        super().__init__()
        for (key, value) in self.__dict__.items():
            if "class" in self[key].widget.attrs:
                self[key].widget.attrs['class'] += 'form-control'
            else:
                self[key].widget.attrs['class'] = 'form-control'