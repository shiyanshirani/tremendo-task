# Generated by Django 3.2.4 on 2021-06-19 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_student_batch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='address',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='phone_number',
        ),
    ]
