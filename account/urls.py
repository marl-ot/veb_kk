from django.urls import path
from account.views import account


urlpatterns = [
    path('', account, name = 'account'),
]