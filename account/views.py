from django.shortcuts import render, redirect
from main.models import Auth, Schools, Classes
from account.forms import UserForm, TeacherForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

@login_required
@transaction.atomic
def account_changes(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            if request.method == 'POST':
                user_form = UserForm(request.POST, instance=request.user)
                teacher_form = TeacherForm(request.POST, instance=request.user)
                if user_form.is_valid() and teacher_form.is_valid():
                    user_form.save()
                    teacher_form.save()
                    messages.success(request, _('Ваш профиль был успешно обновлен!'))
                    return redirect('/')
                else:
                    messages.error(request, _('Пожалуйста, исправьте ошибки.'))
            else:
                user_form = UserForm(instance=request.user)
                teacher_form = TeacherForm(instance=request.user)

    if request.user.is_authenticated:

        user_info = Auth.objects.get(id=request.user.id)
        user_school = Schools.objects.get(id=request.user.school_number_id)

        if request.user.is_teacher:
            
            teacher_classes = Classes.objects.filter(school_id=request.user.school_number_id)
            class_teacher = Classes.objects.filter(teacher_id=request.user.id)

            context = {
                'user_school': user_school,
                'teacher_form': teacher_form,
                'teacher_classes': teacher_classes,
                'class_teacher': class_teacher,
                'user_info': user_info,
            }
        else:

            student_class = Classes.objects.get(id=request.user.user_class_id)
            
            context = {
                'user_school': user_school,
                'user_form': user_form,
                'student_class': student_class,
                'user_info': user_info,
            }
    
        return render(request, 'account/profile.html', context=context)

    return render(request, 'account/profile.html', context=context)


