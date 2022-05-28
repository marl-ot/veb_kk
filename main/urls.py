from django.conf import settings
from django.urls import path
from django.contrib.auth.views import LogoutView
from main.views import (index, LoginUser, RegisterUser, singleMap, book,atlas, active_homework,
                        homeworks, maps, PasswordChangeDoneUser, PasswordChangeUser,
                        PasswordResetCompleteUser, PasswordResetConfirmUser,
                        PasswordResetDoneUser, PasswordResetUser, pageNotFound)
from teacher.views import work_review



urlpatterns = [
    #-------------ученик-----------------------------
    path('', index, name = 'home'),
    path('singleMap/<int:work_id>/', singleMap, name = 'maps'),
    path('homeworks/', homeworks, name = 'homework_list'),
    path('active-homework/', active_homework, name = 'active_homework'),
    path('work_review/<int:student_id>/<int:work_id>/', work_review, name = 'student_review'),
    #-------------общие ссылки--------------------
    #path('about/', about, name = "about"),
    path('book/', book, name = "book"),
    path('atlas/', atlas, name = "atlas"),
    path('contour_map/', maps, name = "contour_map"),
    path('registr/', RegisterUser.as_view(), name = 'registration'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('password-change/', PasswordChangeUser.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneUser.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetUser.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneUser.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmUser.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteUser.as_view(), name='password_reset_complete'),
]

hendler404 = pageNotFound