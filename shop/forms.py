from django import forms


from accounts.Mixins import BootstrapFormMixin
from shop.models import Announcement


class CreateAnnounceForm(forms.ModelForm, BootstrapFormMixin):
    class Meta:
        model = Announcement
        # fields = '__all__'
        exclude = ['seller']
        # widgets = {'seller': TextInput(attrs={
        #     'type': 'text',
        #     'value': '{{ request.user.id }}',
        #     'readonly': ''
        # })}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()
    # NEW = 'Ново'
    # USED = 'Употребявано'
    # CONDITION_TYPES = ((NEW, 'Ново'), (USED, 'Употрябавано'))
    # WORK = "Работа"
    # ELECTRONICS = 'Електроника'
    # CARS = 'Коли'
    # CLOTHES = 'Дрехи'
    # HOME = 'За дома'
    # GiFTS = 'Подаръци'
    # ALL = 'Всички'
    # CATEGORIES_CHOICES = (
    #     (ALL, 'Всички'),
    #     (WORK, 'Работа'),
    #     (ELECTRONICS, 'Електроника'),
    #     (CARS, 'Коли'),
    #     (CLOTHES, 'Дрехи'),
    #     (HOME, 'За дома'),
    #     (GiFTS, 'Подаръци'),
    # )
    #
    # name = forms.CharField(max_length=30, label='Наименование на продукта/услугата')
    # description = forms.CharField(label='Описание на продукта/услугата', widget=forms.Textarea(attrs={
    #     'cols':'40', 'rows': 5, }))
    # image = forms.ImageField(allow_empty_file=True)
    # condition = forms.ChoiceField(choices=CONDITION_TYPES, required=True, label='Състояние')
    # price = forms.IntegerField(max_value=1000000, min_value=1)
    # category = forms.ChoiceField(choices=CATEGORIES_CHOICES, required=True, label='Категория')
    # # seller = forms.CharField(max_length=None, widget=forms.TextInput(attrs={'value': '{{request.user.id}}',}))
