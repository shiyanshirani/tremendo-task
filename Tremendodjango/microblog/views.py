from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    return render(request, 'microblog/home.html')

def login(request):
    return render(request, 'microblog/login.html')

def login_page(request):
    return render(request, 'microblog/login_page.html')