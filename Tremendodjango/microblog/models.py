from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=254)