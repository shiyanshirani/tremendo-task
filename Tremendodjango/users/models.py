from django.db import models

class Student(models.Model):
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'
    GENDER_OPTIONS = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male')
        )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    # photo = models.ImageField(upload_to = "images/")          # pip3 install pillow
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.gender}, {self.address}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.BigIntegerField()
    # photo = models.ImageField(upload_to = "images/")          # pip3 install pillow
    address = models.TextField(blank=True)
    def __str__(self):

        return f"{self.name}, {self.email}, {self.phone_number}, {self.address}"

class Batch(models.Model):
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    total_classes = models.IntegerField() 
    completed_classes = models.IntegerField()

    def __str__(self):
        return f"{self.student}, {self.teacher}, {self.total_classes}, {self.completed_classes}"