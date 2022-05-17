#import time
from django.contrib.auth import login #logout
from django.contrib.auth.views import LoginView #LogoutView
from django.http import HttpResponse, HttpResponseNotFound #Http404
from django.shortcuts import render, redirect #get_object_or_404
from django.urls import reverse_lazy
#from teacher.models import
from django.views.generic import CreateView #FormView, ListView, DetailView 
from main.forms import (UserPasswordChangeForm, LoginUserForm, NewPasswordForm, RegisterUserForm, ResetUserForm)
from django.contrib.auth.views import (PasswordResetDoneView, PasswordChangeView, PasswordResetCompleteView,
PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordChangeDoneView)


def index(request):
    return render(request, 'teacher/index.html')

def about(request):
    return render(request, 'teacher/about.html')

def info(request):
    return HttpResponse('МЕНЮ')

def account_teacher(request):
    return render(request, 'teacher/account.html')

def Teacher_classes(request):
    return render(request, 'teacher/classes.html', )

def pageNotFound():
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

#def show_class(request, num_id):
#    if 4 < num_id < 12:
#        return render(request, 'teacher/class.html')
#    else:
#        return pageNotFound()


def show_class_a(request, num_id):
    if 4 < num_id < 12:
        return render(request, 'teacher/class.html')
    else:
        return pageNotFound()


def show_class_b(request, num_id):
    if 4 < num_id < 12:
        return render(request, 'teacher/class.html')
    else:
        return pageNotFound()


def show_class_c(request, num_id):
    if 4 < num_id < 12:
        return render(request, 'teacher/class.html')
    else:
        return pageNotFound()

    
#---------------------ИЗМЕНЕНИЕ ПАРОЛЯ------------------------
class PasswordChangeUser(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'teacher/password_form_change.html'
    success_url = reverse_lazy("password_change_done_teacher")


class PasswordChangeDoneUser(PasswordChangeDoneView):
    template_name = "teacher/password_change_done.html"
    title = ("Изменение пароля завершено")

#---------------------СБРОС ПАРОЛЯ------------------------

class PasswordResetUser(PasswordResetView):
    form_class = ResetUserForm
    template_name = 'teacher/password_reset_form.html'
    success_url = reverse_lazy("password_reset_done_teacher")


class PasswordResetDoneUser(PasswordResetDoneView):
    template_name = "teacher/password_reset_done.html"
    title = ("Восстановление пароля")


class PasswordResetConfirmUser(PasswordResetConfirmView):
    template_name = "teacher/password_reset_confirm.html"
    form_class = NewPasswordForm
    success_url = reverse_lazy("password_reset_complete_teacher")


class PasswordResetCompleteUser(PasswordResetCompleteView):
    template_name = 'teacher/password_reset_complete.html'
    title = ("Восстановление пароля завершено")

#---------------------РЕГИСТРАЦИЯ------------------------

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'teacher/registr.html'
    success_url = reverse_lazy('login_teacher')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_teacher')

#---------------------АВТОРИЗАЦИЯ------------------------
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'teacher/login.html'

    def get_success_url(self):
        return reverse_lazy('home_teacher')
