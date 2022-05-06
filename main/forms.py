from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm, 
    PasswordChangeForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    PasswordResetForm, SetPasswordForm,
)


class RegisterUserForm(UserCreationForm):
    error_messages = {
        "password_mismatch": ("Пароли не совпадают"),
        'class': ('form-input'),
    }
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    #email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(
        label='Пароль', 
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
        strip=False,
    )
    password2 = forms.CharField(
        label='Повторите пароль', 
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
        strip=False,
    )
    #is_staff = forms.ChoiceField(choices='учитель, ученик')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2') #'email','is_staff'


class LoginUserForm(AuthenticationForm):
    error_messages = {
        "invalid_login": (
            "Пожалуйста введите правильный %(username)s и пароль. Помните, что оба "
            "поля могут быть чувствительны к регистру."
        ),
        "inactive": ("Этот аккаунт не активен."),
    }
    username = forms.CharField(
        label='Логин', 
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        strip=False,
    )
    password = forms.CharField(
        label='Пароль', 
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
        strip=False,
    )


class ResetUserForm(PasswordResetForm):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-input'}),
    )

class ResetUserForm(PasswordResetForm):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-input'}),
    )


class NewPasswordForm(SetPasswordForm):
    error_messages = {
        "password_mismatch": ("Пароли не совпадают"),
    }
    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="Повторите новый пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
    )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Старый пароль', 
        widget=forms.PasswordInput(attrs={'class': 'form-input'}), 
        strip=False,
    )
    new_password1 = forms.CharField(
        label='Новый пароль', 
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
        strip=False,
    )
        
    new_password2 = forms.CharField(
        label='Повторите новый пароль', 
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
        strip=False,
    )
