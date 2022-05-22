from django import forms
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, PasswordChangeForm,)
#from django.contrib.auth.models import User
from django.contrib.auth.forms import (PasswordResetForm, SetPasswordForm,)
from main.models import Auth

""" 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class IsTeacherForm(forms.ModelForm):
    class Meta:
        model = IsTeacher
        fields = ('patronymic', 'school_number', 'birth_date')
"""

#-------------------------РЕГИСТРАЦИЯ-----------------------
class RegisterUserForm(UserCreationForm):
    error_messages = {
        "password_mismatch": ("Пароли не совпадают"),
        'class': ('form-input'),
    }
    username = forms.CharField(
        label='Логин', 
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        strip=False,
    )
    email = forms.EmailField(
        label='Email', 
        widget=forms.EmailInput(attrs={'class': 'form-input'}),
    )
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

    class Meta:
        model = Auth
        fields = ('username', 'email', 'password1', 'password2')

#-----------------АВТОРИЗАЦИЯ-----------------------------

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
    class Meta:
        model = Auth
        fields = ('username', 'password')

#-------------------СБРОС ПАРОЛЯ------------------------

class ResetUserForm(PasswordResetForm):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-input'}),
    )
    class Meta:
        model = Auth
        fields = ('email')

class ResetUserForm(PasswordResetForm):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-input'}),
    )
    class Meta:
        model = Auth
        fields = ('email')

#-----------------ИЗМЕНЕНИЕ ЗАБЫТОГО ПАРОЛЯ----------------------------
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
    class Meta:
        model = Auth
        fields = ('new_password1', 'new_password2')

#--------------------СМЕНА ПАРОЛЯ-----------------------------
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
    class Meta:
        model = Auth
        fields = ('old_password', 'new_password1', 'new_password2')
