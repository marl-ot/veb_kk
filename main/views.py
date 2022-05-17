from django.contrib.auth import login #logout
from django.contrib.auth.views import LoginView #LogoutView
from django.http import HttpResponse, HttpResponseNotFound #Http404
from django.shortcuts import render, redirect #get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import  CreateView #FormView, ListView, DetailView
from main.forms import (UserPasswordChangeForm, LoginUserForm, NewPasswordForm, RegisterUserForm, ResetUserForm)
from django.contrib.auth.views import (PasswordResetDoneView, PasswordChangeView, PasswordResetCompleteView,
PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView,)
#from main.forms import UserForm, IsTeacherForm
#from django.contrib.auth.decorators import login_required
#from django.db import transaction
#from django.contrib import messages

""" 
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        isteacher_form = IsTeacherForm(request.POST, instance=request.user.isteacher)
        if user_form.is_valid() and isteacher_form.is_valid():
            user_form.save()
            isteacher_form.save()
            messages.success(request, _('Ваш профиль был успешно обновлен!'))
            return redirect('settings:profile') #!!!!!!!!!!!!!!!!
        else:
            messages.error(request, _('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserForm(instance=request.user)
        isteacher_form = IsTeacherForm(instance=request.user.isteacher)
    return render(request, 'main/profile.html', {
        'user_form': user_form,
        'isteacher_form': isteacher_form
    })
"""


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def info(request):
    return HttpResponse('МЕНЮ')

def account_student(request):
    return render(request, 'main/account.html')


def singleMap(request):
    return render(request, 'main/singleMap.html')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


#---------------------ИЗМЕНЕНИЕ ПАРОЛЯ------------------------

class PasswordChangeUser(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'main/password_form_change.html'
    success_url = reverse_lazy('password_reset_done')
    
    def get_success_url(self):
        return reverse_lazy('home')


class PasswordChangeDoneUser(PasswordChangeDoneView):
    template_name = "main/password_change_done.html"
    title = ("Изменение пароля завершено")

#-----------------------СБРОС ПАРОЛЯ--------------------------
class PasswordResetUser(PasswordResetView):
    form_class = ResetUserForm
    template_name = 'main/password_reset_form.html'


class PasswordResetDoneUser(PasswordResetDoneView):
    template_name = "main/password_reset_done.html"
    title = ("Восстановление пароля")


class PasswordResetConfirmUser(PasswordResetConfirmView):
    template_name = "main/password_reset_confirm.html"
    form_class = NewPasswordForm


class PasswordResetCompleteUser(PasswordResetCompleteView):
    template_name = 'main/password_reset_complete.html'
    title = ("Восстановление пароля завершено")

#---------------------РЕГИСТРАЦИЯ-----------------------------
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registr.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

#---------------------АВТОРИЗАЦИЯ---------------------------------
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

