from django.conf import settings
from django.urls import path
from teacher.views import Teacher_classes, classwork, homework, show_class_a, show_class_b, show_class_c, class_menu,one_student,homework
from django.contrib.auth.views import LogoutView
from main.views import (LoginUser, RegisterUser, index, info, maps, atlas, about, book,
                        PasswordChangeDoneUser, PasswordChangeUser,
                        PasswordResetCompleteUser, PasswordResetConfirmUser,
                        PasswordResetDoneUser, PasswordResetUser, pageNotFound)




urlpatterns = [
    path('', index, name = 'home_teacher'),
    path('class_menu/',class_menu, name = 'class_menu'),
    path('one_student/',one_student, name = 'one_student'),
    path('classwork/',classwork, name = 'classwork'),
    path('homework/',homework, name = 'homework'),
    path('class/', index, name = 'classes_home_teacher'),
    path('login/', LoginUser.as_view(), name = 'login_teacher'),
    path('registr/', RegisterUser.as_view(), name = 'registr_teacher'),
    path('logout/', LogoutView.as_view(next_page = settings.LOGOUT_REDIRECT_URL), name='logout_teacher'),
    path('book/', book, name = "book"),
    path('atlas/', atlas, name = "atlas"),
    path('contour_map/', maps, name = "contour_map"),
    path('about/', about, name = "about_teacher"),
    #path('class/<int:num_id>/', show_class, name = "num_class"),
    path('class/<int:num_id>/a', show_class_a, name = "num_class_a"),
    path('class/<int:num_id>/b', show_class_b, name = "num_class_b"),
    path('class/<int:num_id>/c', show_class_c, name = "num_class_c"),
    path('password-change/', PasswordChangeUser.as_view(), name='password_change_teacher'),
    path('password-change/done/', PasswordChangeDoneUser.as_view(), name='password_change_done_teacher'),
    path('password-reset/', PasswordResetUser.as_view(), name='password_reset_teacher'),
    path('password-reset/done/', PasswordResetDoneUser.as_view(), name='password_reset_done_teacher'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmUser.as_view(), name='password_reset_confirm_teacher'),
    path('reset/done/', PasswordResetCompleteUser.as_view(), name='password_reset_complete_teacher'),
]

hendler404 = pageNotFound