from django.shortcuts import render
from main.views import pageNotFound
from main.models import Auth, Classes, Schools

def Teacher_classes(request):
    #my_school = request.user.school_number_id.school_num

    classes = Classes.objects.all()
    class_number = Classes.objects.all().values('class_number')
    full = Auth.objects.all()
    schools = Schools.objects.all()
    #class_number = Classes.objects.class_number

    #class_objects(request)

    context =  {
        'classes': classes,
        'full': full,
        'schools': schools,
        'class_number': class_number,
    }

    if request.user.is_teacher:
        return render(request, 'teacher/classes.html', context=context)
    else:
        return pageNotFound(request)

""" 
def class_objects(request):
    classes = Classes.objects.all()
    school_classes = []
    for c in classes:
        if request.user.is_teacher:
            my_school = request.user.school_number_id
            if c.school_id == my_school:
                full_class = str(c.class_number) + str(c.class_letter)
                school_classes.append(full_class)
    return school_classes
"""

#def show_class(request, num_id):
#    if 4 < num_id < 12:
#        if request.user.is_teacher:
#            return render(request, 'teacher/class.html')
#        else:
#            return pageNotFound(request)


def show_class_a(request, num_id):
    if 4 < num_id < 12:
        if request.user.is_teacher:
            return render(request, 'teacher/class.html')
        else:
            return pageNotFound(request)
        
    else:
        return pageNotFound(request)


def show_class_b(request, num_id):
    if 4 < num_id < 12:
        if request.user.is_teacher:
            return render(request, 'teacher/class.html')
        else:
            return pageNotFound(request)


def show_class_c(request, num_id):
    if 4 < num_id < 12:
        if request.user.is_teacher:
            return render(request, 'teacher/class.html')
        else:
            return pageNotFound(request)
