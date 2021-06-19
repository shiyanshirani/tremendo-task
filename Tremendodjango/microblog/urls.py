from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('login/', views.login, name='blog-login'),
    path('register/student', views.register_student, name="student-signup"),
    path('register/teacher', views.register_teacher, name="teacher-signup"),
    path('register/login_page', views.login_page, name="login-page"),
]