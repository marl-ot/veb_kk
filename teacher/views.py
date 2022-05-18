from django.shortcuts import render
from main.views import pageNotFound

def Teacher_classes(request):
    if request.user.is_teacher:
        return render(request, 'teacher/classes.html')
    else:
        return pageNotFound(request)
    

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
