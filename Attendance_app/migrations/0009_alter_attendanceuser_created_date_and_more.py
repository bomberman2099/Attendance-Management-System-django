# Generated by Django 5.0 on 2024-01-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance_app', '0008_alter_attendanceuser_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendanceuser',
            name='created_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='attendanceuser',
            name='end',
            field=models.TimeField(blank=None, null=True),
        ),
        migrations.AlterField(
            model_name='attendanceuser',
            name='start',
            field=models.TimeField(blank=None, null=True),
        ),
    ]