from django.shortcuts import render, redirect
from teacher.forms import GradesForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from main.views import pageNotFound
from main.models import Auth, Classes, Schools, Grades, Works, DoneWorks


def show_class(request, class_id):

    if request.user.is_authenticated:
        if request.user.is_teacher:

            all_students_one_school = Auth.objects.filter(school_number_id = request.user.school_number_id)
            full_class = Classes.objects.filter(id = class_id)[0]
            
            students_class_list = []
            for student in all_students_one_school:
                if student.full_class == full_class:
                    students_class_list.append(student)

            numbers = []
            for i in range(1, len(students_class_list)+1):
                numbers.append(i)
            #print(numbers)


            teacher_classes = Classes.objects.filter(school_id=request.user.school_number_id)
            

            context =  {
                'numbers': numbers,
                'full_class': full_class,
                'class_id': class_id,
                'all_students_one_school': all_students_one_school,
            }
        else:
            context = {
                
            }

        return render(request, 'teacher/class.html', context=context)
        
    return pageNotFound(request)


def class_menu(request, class_id):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            
            full_class = list(Classes.objects.filter(id = class_id))[0]

            context =  {
                'full_class': full_class,
                'class_id': class_id,
            }
        else:
            context = {
                
            }

        return render(request, 'teacher/class_menu.html', context=context)
        
    return pageNotFound(request)


def one_student(request, student_id):

    if request.user.is_authenticated:
        if request.user.is_teacher:
            teacher = Auth.objects.filter(id=request.user.id)[0]
            works = Works.objects.filter(teacher_id=teacher.id)
            done_works = DoneWorks.objects.filter(student_id=student_id)
            #print(works)
            student = Auth.objects.filter(id = student_id)[0]

            context =  {
                'student': student,
            }
            
        else:
            context = {
                
            }

        return render(request, 'teacher/one_student.html', context=context)
        
    return pageNotFound(request)

def undone_work(request, class_id):
    if request.user.is_authenticated:
        if request.user.is_teacher:

            comment_grade = Grades.objects.all()

            #classes = Classes.objects.filter(id = class_id)[0]
            all_students_one_school = Auth.objects.filter(school_number_id=request.user.school_number_id)
            full_class = Classes.objects.filter(id=class_id)[0]

            students_list = []

            students_class_list = []
            for student in all_students_one_school:
                if student.full_class == full_class:
                    for i in comment_grade:
                        if student.id == i.student.id:
                            students_class_list.append(student)

            numbers = []
            for i in range(1, len(students_class_list)+1):
                numbers.append(i)
            #print(numbers)


            teacher_classes = Classes.objects.filter(school_id=request.user.school_number_id)
            

            context =  {
                'students_class_list': students_class_list,
                'comment_grade': comment_grade,
                'numbers': numbers,
                'full_class': full_class,
                'class_id': class_id,
                'all_students_one_school': all_students_one_school,
            }
        else:
            context = {
                
            }

        return render(request, 'teacher/undone_work.html', context=context)
        
    return pageNotFound(request)

@login_required
@transaction.atomic
def work_review(request, student_id, work_id):
    if request.method == 'POST':
        grades_form = GradesForm(request.POST, instance=request.user)
        if grades_form.is_valid():
            grades_form.save()
            messages.success(request, _('Ваш профиль был успешно обновлен!'))
            if request.user.is_teacher == True:
                return redirect('home_teacher')
            else:
                return pageNotFound(request)
        else:
            messages.error(request, _('Пожалуйста, исправьте ошибки.'))
    else:
        grades_form = GradesForm(instance=request.user)

    if request.user.is_authenticated:
        if request.user.is_teacher:
            
            #comment_grade = Grades.objects.filter(student_id = student_id)[0]
            student = Auth.objects.filter(id = student_id)[0]
            grades = Grades.objects.all()
            done_works = DoneWorks.objects.filter(id=work_id, student_id=student_id)[0]
            works = Works.objects.filter(id=work_id)[0]
            my_school = Schools.objects.filter(id=request.user.school_number_id)[0]
            #print(done_works.student_id)
            #print(my_school)
            context =  {
            #    'comment_grade': comment_grade,
                'done_works': done_works,
                'student': student,
                'grades_form': grades_form,
                'works': works,
                'student_id': student_id,
                'work_id': work_id,
                'my_school': my_school,
            }

        else:
            context = {
                
            }

        return render(request, 'teacher/work_review.html', context=context)
        
    return pageNotFound(request)
    
def homework(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:

            context =  {

            }
        else:
            context = {
                
            }
        return render(request, 'teacher/homework.html', context=context)
    return pageNotFound(request)

def classwork(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:

            context =  {

            }
        else:
            context = {
                
            }
        return render(request, 'teacher/classwork.html', context=context)
    return pageNotFound(request)