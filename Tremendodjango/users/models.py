from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'
    GENDER_OPTIONS = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male')
        )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True)
    # photo = models.ImageField(upload_to = "images/")          # pip3 install pillow
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.gender}, {self.address}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.BigIntegerField(blank=True, default=0)
    # photo = models.ImageField(upload_to = "images/")          # pip3 install pillow
    address = models.TextField(blank=True)
    def __str__(self):

        return f"{self.name}, {self.email}, {self.phone_number}, {self.address}"

class Batch(models.Model):
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    total_classes = models.IntegerField(default=10) 
    completed_classes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.students}, {self.teacher}, {self.total_classes}, {self.completed_classes}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}, Profile"
