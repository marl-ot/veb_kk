from django.conf import settings
from django.urls import path
from django.contrib.auth.views import LogoutView
from main.views import (index, LoginUser, RegisterUser, singleMap, book,atlas, maps,
                        info, about, PasswordChangeDoneUser, PasswordChangeUser,
                        PasswordResetCompleteUser, PasswordResetConfirmUser,
                        PasswordResetDoneUser, PasswordResetUser, pageNotFound)



urlpatterns = [
    path('', index, name = 'home'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('registr/', RegisterUser.as_view(), name = 'registration'),
    path('singleMap/', singleMap, name = 'maps'),
    path('logout/', LogoutView.as_view(next_page = settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('book/', book, name = "book"),
    path('atlas/', atlas, name = "atlas"),
    path('contour_map/', maps, name = "contour_map"),
    path('about/', about, name = "about"),
    path('password-change/', PasswordChangeUser.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneUser.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetUser.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneUser.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmUser.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteUser.as_view(), name='password_reset_complete'),
]

hendler404 = pageNotFound