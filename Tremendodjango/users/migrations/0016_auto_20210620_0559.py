# Generated by Django 3.2.4 on 2021-06-20 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20210620_0541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='student',
        ),
        migrations.AddField(
            model_name='batch',
            name='student',
            field=models.ManyToManyField(to='users.Student'),
        ),
    ]
