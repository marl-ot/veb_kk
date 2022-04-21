from django.conf import settings
from django.urls import path
from main.views import *


urlpatterns = [
    path('', index, name = 'home'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('registr/', RegisterUser.as_view(), name = 'registration'),
    path('singleMap/', singleMap, name = 'first map'),
    path('logout/', LogoutView.as_view(next_page = settings.LOGOUT_REDIRECT_URL), name='logout')
]

hendler404 = pageNotFound
