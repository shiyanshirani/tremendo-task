# Generated by Django 3.2.4 on 2021-06-20 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_batch'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
