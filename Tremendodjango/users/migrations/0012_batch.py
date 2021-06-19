# Generated by Django 3.2.4 on 2021-06-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_student_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=100)),
                ('student', models.CharField(max_length=100)),
                ('total_classes', models.IntegerField()),
                ('completed_classes', models.IntegerField()),
            ],
        ),
    ]