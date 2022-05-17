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
            if request.user.is_teacher == True:
                return redirect('home_teacher')
            else:
                return redirect('home')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
    else:
        profile_form = ProfileForm(instance=request.user)
    return render(request, 'account/profile.html', {'profile_form': profile_form})
