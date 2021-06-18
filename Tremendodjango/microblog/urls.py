from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('login/', views.login, name='blog-login'),
    path('register/student', views.register_student, name="student-signup")
]