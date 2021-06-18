from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'microblog/home.html')

def login(request):
    return render(request, 'microblog/login.html')

# def student_signup(request):
#     return render(request, 'microblog/student_signup.html')

def register_student(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()
    return render(request, 'microblog/register.html', {'form': form})