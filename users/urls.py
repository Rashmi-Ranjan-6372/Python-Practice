from django import views
from django.urls import include, path
from . import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view()),
    path('details/', views.UserDetailsView.as_view()),
    path('details/<int:pk>/', views.UserDetailsView.as_view()),
    path('update/<int:pk>/', views.UserUpdateView.as_view()),
    path('delete/<int:pk>/', views.UserDeleteView.as_view()),
]