from django.urls import path
from ratings import views


urlpatterns = [
    path('', views.ratings, name = 'ratings'),
    path('editing/', views.editing, name = 'editing'),
    path('<int:pk>/', views.StudentsDetailView.as_view(), name = 'students'),
    path('<int:pk>/update/', views.StudentsUpdateView.as_view(), name = 'students-update'),
    path('<int:pk>/delete/', views.StudentsDeleteView.as_view(), name = 'students-delete')
]