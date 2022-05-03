from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from main.models import Classes
from django.views.generic import ListView, DetailView, CreateView, FormView
from main.forms import *

menu = [{'title': "Карты", 'url_name': 'maps'},
        {'title': "Меню", 'url_name': 'maps'},
        {'title': "О нас", 'url_name': 'maps'},
        {'title': "Войти", 'url_name': 'maps'}
]


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse('О НАС')

def info(request):
    return HttpResponse('МЕНЮ')

#def login(request):
#    return render(request, 'main/login.html')

def singleMap(request):
    return render(request, 'main/singleMap.html')

def Teacher_index(request):
    return render(request, 'main/teacher/index.html')

def Teacher_classes(request):
    return render(request, 'main/teacher/classes.html', )

#def Single_class(request, num_id):
#    return render(request, 'main/teacher/singleClass.html')

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_class(request, num_id):
    return render(request, 'main/teacher/singleClass.html') #HttpResponse(f"Отображение класса с id = {num_id}")

class RegisterUser (CreateView):
    form_class = UserCreationForm
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

'''
class LoginTeacher(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('teacher')
'''