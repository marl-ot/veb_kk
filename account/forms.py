from main.models import Auth
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, DateInput

class UserForm(ModelForm):
    class Meta:
        model = Auth
        fields = ['username', 'first_name', 'last_name', 'patronymic', 'birth_date', 'email']

        widgets = {
            'username': TextInput(attrs ={
                'class': 'form control',
                'placeholder': 'Логин'
            }),
            'first_name': TextInput(attrs ={
                'class': 'form control',
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'form control',
                'placeholder': 'Фамилия'
            }),
            'patronymic': TextInput(attrs={
                'class': 'form control',
                'placeholder': 'Отчество'
            }),
            'email': EmailInput(attrs={
                'class':'form control',
                'placeholder':'Почта'
            }),
            'birth_date': DateInput(attrs={
                'class':'form control',
                'placeholder':'Дата рождения'
            }),
        }


class TeacherForm(ModelForm):
    class Meta:
        model = Auth
        fields = ['username', 'first_name', 'last_name', 'patronymic', 'email']

        widgets = {
            'username': TextInput(attrs ={
                'class': 'form control',
                'placeholder': 'Логин'
            }),
            'first_name': TextInput(attrs ={
                'class': 'form control',
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'form control',
                'placeholder': 'Фамилия'
            }),
            'patronymic': TextInput(attrs={
                'class': 'form control',
                'placeholder': 'Отчество'
            }),
            'email': EmailInput(attrs={
                'class':'form control',
                'placeholder':'Почта'
            }),
        }