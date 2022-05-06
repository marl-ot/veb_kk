from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from main.models import Classes
from django.views.generic import (ListView, DetailView, CreateView, FormView)
from main.forms import (UserPasswordChangeForm, LoginUserForm, NewPasswordForm, RegisterUserForm, ResetUserForm)
from django.contrib.auth.views import (PasswordResetDoneView, PasswordChangeView, PasswordResetCompleteView,
PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView,)


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def info(request):
    return HttpResponse('МЕНЮ')

def account_student(request):
    return render(request, 'main/account.html')

#def account_teacher(request):
#    return render(request, 'main/teacher/account.html')

#def login(request):
#    return render(request, 'main/login.html')

def singleMap(request):
    return render(request, 'main/singleMap.html')

#def Teacher_index(request):
#    return render(request, 'main/teacher/index.html')

#def Teacher_classes(request):
#    return render(request, 'main/teacher/classes.html', )

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

#def show_class(request, num_id):
#    return render(request, 'main/teacher/class.html')

class PasswordChangeUser(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'main/password_form_change.html'
    success_url = reverse_lazy('about')
    
    def get_success_url(self):
        return reverse_lazy('home')


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


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registr.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
