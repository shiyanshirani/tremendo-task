from django.db import models

class Student(models.Model):
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'
    GENDER_OPTIONS = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male'),)
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    # photo = models.ImageField(upload_to = "images/")
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)