

from django.urls import path, include

from . import views

urlpatterns = [
    path('log-in/', views.LogIn.as_view()),
    path('sign-up/', views.SignUp.as_view()),
]
