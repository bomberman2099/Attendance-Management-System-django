# Generated by Django 5.0 on 2024-01-04 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserRegister',
            new_name='UserProfile',
        ),
    ]
