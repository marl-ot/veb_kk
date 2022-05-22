from django.shortcuts import render
from main.views import pageNotFound
from main.models import Auth, Classes, Schools


def show_class(request, class_id):

    if request.user.is_authenticated:
        if request.user.is_teacher:
            #classes = Classes.objects.filter(id = class_id)[0]
            all_students_one_school = Auth.objects.filter(school_number_id = request.user.school_number_id)
            full_class = Classes.objects.filter(id = class_id)[0]
            
            students_class_list = []
            for student in all_students_one_school:
                if student.full_class == full_class:
                    students_class_list.append(student)

            numbers = []
            for i in range(1, len(students_class_list)+1):
                numbers.append(i)
            print(numbers)


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


    # if 4 < num_id < 12:
    #     if request.user.is_teacher:
    #         return render(request, 'teacher/class.html')
    #     else:
    #         return pageNotFound(request)


# def show_class_a(request, num_id):
#     if 4 < num_id < 12:
#         if request.user.is_teacher:
#             return render(request, 'teacher/class.html')
#         else:
#             return pageNotFound(request)

#     else:
#         return pageNotFound(request)


# def show_class_b(request, num_id):
#     if 4 < num_id < 12:
#         if request.user.is_teacher:
#             return render(request, 'teacher/class.html')
#         else:
#             return pageNotFound(request)


# def show_class_c(request, num_id):
#     if 4 < num_id < 12:
#         if request.user.is_teacher:
#             return render(request, 'teacher/class.html')
#         else:
#             return pageNotFound(request)


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

            #classes = Classes.objects.filter(id = class_id)[0]
            all_students_one_school = Auth.objects.filter(school_number_id = request.user.school_number_id)
            full_class = Classes.objects.filter(id = class_id)[0]
            
            students_class_list = []
            for student in all_students_one_school:
                if student.full_class == full_class:
                    students_class_list.append(student)

            numbers = []
            for i in range(1, len(students_class_list)+1):
                numbers.append(i)
            print(numbers)


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

        return render(request, 'teacher/undone_work.html', context=context)
        
    return pageNotFound(request)


def work_review(request, student_id):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            
            students = Auth.objects.filter(id = student_id)[0]

            context =  {
                
                #'student_id': student_id,
                'students': students,
            }
        else:
            context = {
                
            }

        return render(request, 'teacher/work_review.html', context=context)
        
    return pageNotFound(request)
    
def homework(request):
    return render(request, 'teacher/homework.html')

def classwork(request):
    return render(request, 'teacher/classwork.html')