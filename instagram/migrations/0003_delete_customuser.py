# Generated by Django 3.2 on 2021-05-23 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]