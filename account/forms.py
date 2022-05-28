from main.models import Auth
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, DateInput

class UserForm(ModelForm):
    class Meta:
        model = Auth
        fields = ['username', 'birth_date', 'email']# 'first_name', 'last_name', 'patronymic', 'email'

        widgets = {
            'username': TextInput(attrs ={
                'class': 'info-span form control',
                'placeholder': 'Логин'
            }),
            # 'first_name': TextInput(attrs ={
            #     'class': 'form control',
            #     'placeholder': 'Имя'
            # }),
            # 'last_name': TextInput(attrs={
            #     'class': 'form control',
            #     'placeholder': 'Фамилия'
            # }),
            # 'patronymic': TextInput(attrs={
            #     'class': 'form control',
            #     'placeholder': 'Отчество'
            # }),
            'email': EmailInput(attrs={
                'class':'info-span',
                'placeholder':'Почта'
            }),
            'birth_date': DateInput(attrs={
                'class':'info-span',
                'placeholder':'Дата рождения'
            }),
        }


class TeacherForm(ModelForm):
    class Meta:
        model = Auth
        fields = ['username', 'email'] # 'first_name', 'last_name', 'patronymic'

        widgets = {
            'username': TextInput(attrs ={
                'class': 'info-span',
                'placeholder': 'Логин'
            }),
            # 'first_name': TextInput(attrs ={
            #     'class': 'form control',
            #     'placeholder': 'Имя'
            # }),
            # 'last_name': TextInput(attrs={
            #     'class': 'form control',
            #     'placeholder': 'Фамилия'
            # }),
            # 'patronymic': TextInput(attrs={
            #     'class': 'form control',
            #     'placeholder': 'Отчество'
            # }),
            'email': EmailInput(attrs={
                'class':'info-span',
                'placeholder':'Почта'
            }),
        }