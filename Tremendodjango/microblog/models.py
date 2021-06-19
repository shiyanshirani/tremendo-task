from django.db import models
from phone_field import PhoneField

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.BigIntegerField()
    # photo = models.ImageField(upload_to = "images/") # pip3 install pillow
    address = models.TextField()

class Student(models.Model):
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'
    GENDER_OPTIONS = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male')
        )
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    # photo = models.ImageField(upload_to = "images/") # pip3 install pillow
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    address = models.TextField()
    batch_enrolled = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.gender}, {self.address}"