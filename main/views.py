from operator import is_
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import  CreateView
from main.forms import (UserPasswordChangeForm, LoginUserForm, NewPasswordForm, RegisterUserForm, ResetUserForm)
from django.contrib.auth.views import (PasswordResetDoneView, PasswordChangeView, PasswordResetCompleteView,
PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView,)
from main.models import Classes, Schools, Auth, Works


def index(request):
    if request.user.is_authenticated:

        works = Works.objects.filter()

        if request.user.is_teacher:

            teacher_classes = Classes.objects.filter(school_id=request.user.school_number_id)

            context =  {
                'teacher_classes': teacher_classes,
            }

        else:

            is_active = False
            for w in works:
                if w.is_active == 1:
                    is_active = True

            print(is_active)

            context = {
                'is_active': is_active,
            }

        return render(request, 'main/index.html', context=context)
        
    return render(request, 'main/index.html')

def book(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:

            context =  {

            }
        else:
            context = {
                
            }
        return render(request, 'main/books.html', context=context)

    return render(request, 'main/books.html')

def atlas(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:

            context =  {

            }
        else:
            context = {
                
            }
        return render(request, 'main/atlases.html', context=context)

    return render(request, 'main/atlases.html')

def maps(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:

            context =  {

            }
        else:
            context = {
                
            }
        return render(request, 'main/maps.html', context=context)

    return render(request, 'main/maps.html')

# def about(request):
#     return render(request, 'main/about.html')

def info(request):
    return HttpResponse('МЕНЮ')
    
def active_homework(request):
    if request.user.is_authenticated:
        if request.user.is_teacher == False:
            works = Works.objects.filter()

            context = {
                'works': works,
            }

        else:
            context = {}
        return render(request, 'main/active_homework.html', context=context)

    return pageNotFound(request)

def homeworks(request):
    if request.user.is_authenticated:
        if request.user.is_teacher == False:
            works = Works.objects.filter()
            is_active = 0
            for w in works:
                if w.is_active:
                    is_active += 1
            #print(works)
            context = {
                'works': works,
                'is_active': is_active,
            }
        else:
            context = {}
        return render(request, 'main/homework.html', context=context)

    return pageNotFound(request)

def singleMap(request, work_id):
    if request.user.is_authenticated:
        if request.user.is_teacher == False:
            works = Works.objects.filter(id = work_id)
            for i in works:
                location_link = i.work
            #print(location_link)
            context = {
                'works': works,
                'location_link': location_link,
            }
        else:
            context = {}
        return render(request, 'main/singleMap.html', context=context)

    return pageNotFound(request)

def pageNotFound(request, **kwargs):
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

