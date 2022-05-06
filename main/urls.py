from django.conf import settings
from django.urls import path
from main.views import *
from django.contrib.auth import views



urlpatterns = [
    path('', index, name = 'home'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('registr/', RegisterUser.as_view(), name = 'registration'),
    path('singleMap/', singleMap, name = 'maps'),
    path('teacher/', Teacher_index, name = 'teacher'),
    path('teacher/classes/', Teacher_classes, name = 'classes'),
    path('logout/', LogoutView.as_view(next_page = settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('menu/', info, name = "menu"),
    path('about/', about, name = "about"),
    path('teacher/class/<int:num_id>/', show_class, name = "num_class"),
    path('user/password-change/', PasswordChangeUser.as_view(), name='password_change'),
    path('user/password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('account/', account_student, name = 'account_student'),
    path('teacher/account/', account_teacher, name = 'account_teacher'),
    path('user/password-reset/', PasswordResetUser.as_view(), name='password_reset'),
    path('user/password-reset/done/', PasswordResetDoneUser.as_view(), name='password_reset_done'),
    path('user/reset/<uidb64>/<token>/', PasswordResetConfirmUser.as_view(), name='password_reset_confirm'),
    path('user/reset/done/', PasswordResetCompleteUser.as_view(), name='password_reset_complete'),
]

hendler404 = pageNotFound
