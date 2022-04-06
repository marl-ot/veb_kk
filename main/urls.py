from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('index/', views.index),
    path('login/', views.login),
    path('reg/', views.registr)
]