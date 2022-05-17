from django.conf import settings
from django.urls import path
from main.views import *
#from django.contrib.auth import views



urlpatterns = [
    path('', index, name = 'home'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('registr/', RegisterUser.as_view(), name = 'registration'),
    path('singleMap/', singleMap, name = 'maps'),
    path('logout/', LogoutView.as_view(next_page = settings.LOGOUT_REDIRECT_URL_STUDENT), name='logout'),
    path('menu/', info, name = "menu"),
    path('about/', about, name = "about"),
    path('password-change/', PasswordChangeUser.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneUser.as_view(), name='password_change_done'),
    path('account/', account_student, name = 'account_student'),
    path('password-reset/', PasswordResetUser.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneUser.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmUser.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteUser.as_view(), name='password_reset_complete'),
]

hendler404 = pageNotFound