from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation

class SignUpStudent(UserCreationForm):
    full_name = forms.CharField(max_lenth=50, min_length=4, required=True, help_text="Full Name")
