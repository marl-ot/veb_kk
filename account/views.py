from django.shortcuts import render, redirect
from main.models import Auth
from account.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
#from django.utils.translation import ugettext_lazy as _


@login_required
@transaction.atomic
def account(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!'))
            return redirect('home')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
    else:
        profile_form = ProfileForm(instance=request.user)
    return render(request, 'account/profile.html', {
        'profile_form': profile_form
    })


#def account(request):
#    return render(request, 'account/profile.html')
"""
def account(request):
    error = ''
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была заполнена неверно'

    form = ProfileForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'account/profile.html', context=context)
"""
""" 
def account(request, user_id):
    user = Auth.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()
"""