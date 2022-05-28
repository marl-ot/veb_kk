from turtle import done
from django.shortcuts import render, redirect
from teacher.forms import GradesForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from main.views import pageNotFound
from main.models import Auth, Classes, Schools, Works, DoneWorks


def show_class(request, class_id):

    if request.user.is_authenticated:
        if request.user.is_teacher:
            
            all_students_one_school = Auth.objects.filter(school_number_id = request.user.school_number_id)
            full_class = Classes.objects.get(id = class_id)
            done_works = DoneWorks.objects.filter(teacher_id = request.user.id)
            #works = Works.objects.filter(id = done_works.work_id)
            students_class_list = []
            for student in all_students_one_school:
                if student.user_class_id == class_id:
                    students_class_list.append(student)

            uncheck_works = 0
            num = 0
            mean = 0
            for w in done_works:
                num += 1
                mean += w.grade
                if w.grade == None:
                    uncheck_works += 1
            mean_grade = mean/num

            numbers = []
            for i in range(1, len(students_class_list)+1):
                numbers.append(i)
            #print(numbers)


            #teacher_classes = Classes.objects.filter(school_id=request.user.school_number_id)
            

            context =  {
                #'works': works,
                'mean_grade': mean_grade,
                'uncheck_works': uncheck_works,
                'numbers': numbers,
                'done_works': done_works,
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
            
            full_class = Classes.objects.get(id = class_id)
            #print(full_class)
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
            teacher = Auth.objects.get(id=request.user.id)
            works = Works.objects.filter(teacher_id=teacher.id)
            done_works = DoneWorks.objects.filter(student_id=student_id)
            student = Auth.objects.get(id = student_id)
            student_class = Classes.objects.get(id = student.user_class_id)

            students_works_list = []
            for s in done_works:
                if s.student_id == student_id:
                    students_works_list.append(s)

            numbers = []
            for i in range(1, len(students_works_list)+1):
                numbers.append(i)

            context =  {
                'student_class': student_class,
                'numbers': numbers,
                'works': works,
                'done_works': done_works,
                'student_id': student_id,
                'student': student,
            }
            
        else:
            context = {
                
            }

        return render(request, 'teacher/one_student.html', context=context)
        
    return pageNotFound(request)


# def class_generate(request):
#     classes_dict = {}
#     all_students = Auth.objects.filter(is_teacher=False)#, is_superuser=False, is_staff=False
#     db_class = Classes.objects.filter(school_id = request.user.school_number_id)
#     for student in all_students:
#         s_class = student.user_class_id
#         #print(s_class)
#         for c in db_class:
#             if s_class == c.id:
#                 classes_dict[str(student.last_name) + ' ' + str(student.first_name) + ' ' + str(student.patronymic)]=str(c.class_number) + str(c.class_letter)
#     #print(classes_dict)
            


def undone_work(request, class_id):
    if request.user.is_authenticated:
        if request.user.is_teacher:

            
            all_students_one_school = Auth.objects.filter(school_number_id=request.user.school_number_id)
            full_class = Classes.objects.get(id=class_id)
            done_works = DoneWorks.objects.filter(teacher_id=request.user.id)
            #print(class_generate(request))
            students_list = []
            
            # students_class_list = []
            # for student in all_students_one_school:
            #     if student.user_class_id == class_id:
            #         for i in done_works:
            #             if student.id == i.student_id:
            #                 students_class_list.append(student)

            # numbers = []
            # for i in range(1, len(students_class_list)+1):
            #     numbers.append(i)
            #print(numbers)


            #teacher_classes = Classes.objects.filter(school_id=request.user.school_number_id)
            

            context =  {
                # 'students_class_list': students_class_list,
                # 'numbers': numbers,
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
    if request.user.is_authenticated:
        if request.user.is_teacher:
            done_works = DoneWorks.objects.get(id=student_id, work_id=work_id)
            if request.method == 'POST':
                grades_form = GradesForm(request.POST, instance=done_works)
                if grades_form.is_valid():
                    grades_form.save()
                    messages.success(request, _('Ваш профиль был успешно обновлен!'))
                    if request.user.is_teacher == True:
                        return redirect('/')
                    else:
                        return pageNotFound(request)
                else:
                    messages.error(request, _('Пожалуйста, исправьте ошибки.'))
            else:
                grades_form = GradesForm(instance=done_works)


    if request.user.is_authenticated:
        if request.user.is_teacher:
            print(done_works)
            student = Auth.objects.get(id=student_id)
            done_works = DoneWorks.objects.filter(id=work_id, student_id=student_id)
            works = Works.objects.get(id=work_id, teacher_id=request.user.id)
            my_school = Schools.objects.get(id=request.user.school_number_id)
            student_class = Classes.objects.get(id=student_id)
    
            context =  {
                'student_class': student_class,
                'done_works': done_works,
                'student': student,
                'grades_form': grades_form,
                'works': works,
                'student_id': student_id,
                'work_id': work_id,
                'my_school': my_school,
            }

        else:

            student = Auth.objects.get(id=student_id)
            done_works = DoneWorks.objects.get(id=work_id, student_id=student_id)
            works = Works.objects.get(id=work_id)
            my_school = Schools.objects.get(id=request.user.school_number_id)
            student_class = Classes.objects.get(id=student_id)

            context = {
                'student_class': student_class,
                'done_works': done_works,
                'student': student,
                'works': works,
                'grades_form': grades_form,
                'student_id': student_id,
                'work_id': work_id,
                'my_school': my_school,
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