from django.urls import path
from account.views import account_changes


urlpatterns = [
    path('', account_changes, name = 'account'),
]