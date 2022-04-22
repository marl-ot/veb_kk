from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from main.forms import *


def index(request):
    return render(request, 'main/index.html')


#def login(request):
#    return render(request, 'main/login.html')

def singleMap(request):
    return render(request, 'main/singleMap.html')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


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

