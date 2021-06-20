from django.contrib import admin

# Register your models here.
from .models import Teacher, Student, Batch, Profile

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Batch)
admin.site.register(Profile)

