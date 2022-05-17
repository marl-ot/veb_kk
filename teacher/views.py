from django.shortcuts import render
from main.views import pageNotFound

def Teacher_classes(request):
    return render(request, 'teacher/classes.html')

#def show_class(request, num_id):
#    if 4 < num_id < 12:
#        return render(request, 'teacher/class.html')
#    else:
#        return pageNotFound()


def show_class_a(request, num_id):
    if 4 < num_id < 12:
        return render(request, 'teacher/class.html')
    else:
        return pageNotFound()


def show_class_b(request, num_id):
    if 4 < num_id < 12:
        return render(request, 'teacher/class.html')
    else:
        return pageNotFound()


def show_class_c(request, num_id):
    if 4 < num_id < 12:
        return render(request, 'teacher/class.html')
    else:
        return pageNotFound()
