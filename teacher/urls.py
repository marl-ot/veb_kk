from django.urls import path
from main.views import index, pageNotFound
from teacher.views import (classwork, undone_work, homework, show_class, class_menu, one_student, work_review, homework)





urlpatterns = [
    path('', index, name = 'teacher_classes'),
    path('class_menu/<int:class_id>/', class_menu, name = 'class_menu'),
    path('student/<int:student_id>/', one_student, name = 'one_student'),
    path('undone_work/<int:class_id>/', undone_work, name = 'undone_work'),
    path('work_review/<int:student_id>/<int:work_id>/', work_review, name = 'work_review'),
    path('classwork/', classwork, name = 'classwork'),
    path('homework/', homework, name = 'homework'),
    path('my_class/<int:class_id>/', show_class, name = "one_class"),
    #path('class/<int:num_id>/a', show_class_a, name = "num_class_a"),
    #path('class/<int:num_id>/b', show_class_b, name = "num_class_b"),
    #path('class/<int:num_id>/c', show_class_c, name = "num_class_c"),
]

hendler404 = pageNotFound