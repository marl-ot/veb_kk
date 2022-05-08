from django.urls import path
from raitings import views


urlpatterns = [
    path('', views.raitings, name = 'raitings'),
    path('editing/', views.editing, name = 'editing'),
    path('student/<int:pk>/', views.StudentsDetailView.as_view(), name = 'students'),
    path('student/<int:pk>/update/', views.StudentsUpdateView.as_view(), name = 'students-update'),
    path('student/<int:pk>/delete/', views.StudentsDeleteView.as_view(), name = 'students-delete')
]