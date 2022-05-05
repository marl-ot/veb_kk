from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from main.models import Classes
from django.views.generic import ListView, DetailView, CreateView, FormView
from main.forms import UserPasswordChangeForm, LoginUserForm, RegisterUserForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

menu = [{'title': "Карты", 'url_name': 'maps'},
        {'title': "Меню", 'url_name': 'maps'},
        {'title': "О нас", 'url_name': 'maps'},
        {'title': "Войти", 'url_name': 'maps'}
]


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def info(request):
    return HttpResponse('МЕНЮ')

def account_student(request):
    return render(request, 'main/account.html')

def account_teacher(request):
    return render(request, 'main/teacher/account.html')

#def login(request):
#    return render(request, 'main/login.html')

def singleMap(request):
    return render(request, 'main/singleMap.html')

def Teacher_index(request):
    return render(request, 'main/teacher/index.html')

def Teacher_classes(request):
    return render(request, 'main/teacher/classes.html', )

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_class(request, num_id):
    return render(request, 'main/teacher/singleClass.html')

class PasswordChangeUser(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'main/password_form_change.html'
    success_url = reverse_lazy('login')
    
    def get_success_url(self):
        return reverse_lazy('home')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registr.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

'''
def a_change_password(request):
    u = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = request.POST.get("old_password")
            new_pass = request.POST.get("new_password")
            new_pass_rep = request.POST.get("new_password_repeat")
            if check_password(old_password, u.password):
                return HttpResponse('ok')
            else:
                return HttpResponse('bad')
    else:
            form = ChangePasswordForm()

    return render(request, 'login/change_password.html',
              {'form': form, 'user': u})
'''

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