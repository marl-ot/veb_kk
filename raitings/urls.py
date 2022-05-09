from django.urls import path
from raitings import views


urlpatterns = [
    path('', views.raitings, name = 'raitings'),
    path('editing/', views.editing, name = 'editing'),
    path('<int:pk>/', views.StudentsDetailView.as_view(), name = 'students'),
    path('<int:pk>/update/', views.StudentsUpdateView.as_view(), name = 'students-update'),
    path('<int:pk>/delete/', views.StudentsDeleteView.as_view(), name = 'students-delete')
]