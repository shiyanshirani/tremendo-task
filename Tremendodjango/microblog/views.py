from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'microblog/home.html')

def login(request):
    return render(request, 'microblog/login.html')

def register_student(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
    else:
        form = UserCreationForm()
    return render(request, 'microblog/register_student.html', {'form': form})

def register_teacher(request):
    return render(request, 'microblog/register_teacher.html')

def login_page(request):
    return render(request, 'microblog/login_page.html')