# Generated by Django 5.0 on 2024-01-05 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance_app', '0002_alter_attendanceuser_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendanceuser',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]