from django.urls import path
from main.views import *


urlpatterns = [
    path('', index, name = 'home'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('registr/', RegisterUser.as_view(), name = 'registration'),
    path('singleMap/', singleMap, name = 'first map'),
    path('logout/', logout_user, name = "logout")
]

hendler404 = pageNotFound
