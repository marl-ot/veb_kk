from ratings.models import Articles
from django.forms import ModelForm, TextInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['surname', 'name', 'patronymic', 'estimation','task']

        widgets = {
            'surname': TextInput(attrs ={
                'class': 'form control',
                'placeholder': 'Фамилия'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'patronymic': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            'task': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Задание'
            })
        }