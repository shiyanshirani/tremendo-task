from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'microblog/home.html')

def login(request):
    return render(request, 'microblog/login.html')

def login_page(request):
    return render(request, 'microblog/login_page.html')