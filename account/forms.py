from main.models import Auth
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, DateInput

class ProfileForm(ModelForm):
    class Meta:
        model = Auth
        fields = ['first_name', 'last_name', 'patronymic', 'school_number', 'birth_date', 'email']

        widgets = {
            'first_name': TextInput(attrs ={
                'class': 'form control',
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'patronymic': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            'email': EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Почта'
            }),
            'school_number': NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Номер школы'
            }),
            'birth_date': DateInput(attrs={
                'class':'form-control',
                'placeholder':'Дата рождения'
            }),
        }