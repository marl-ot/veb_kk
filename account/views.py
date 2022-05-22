from django.shortcuts import render, redirect
from main.models import Auth
from account.forms import UserForm, TeacherForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


@login_required
@transaction.atomic
def account(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        teacher_form = TeacherForm(request.POST, instance=request.user)
        if user_form.is_valid() and teacher_form.is_valid():
            user_form.save()
            teacher_form.save()
            messages.success(request, _('Ваш профиль был успешно обновлен!'))
            if request.user.is_teacher == True:
                return redirect('home_teacher')
            else:
                return redirect('home')
        else:
            messages.error(request, _('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserForm(instance=request.user)
        teacher_form = TeacherForm(instance=request.user)
    return render(request, 'account/profile.html', {'user_form': user_form, 'teacher_form': teacher_form})
