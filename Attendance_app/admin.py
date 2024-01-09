from django.contrib import admin
<<<<<<< HEAD
from . import models


admin.site.register(models.AttendanceUser)
=======
from .models import AttendanceUser

class AttendanceUserAdmin(admin.ModelAdmin):
    fields = ('user', 'created_date', 'start', 'end', 'job_time')


admin.site.register(AttendanceUser, AttendanceUserAdmin)
>>>>>>> 15a2cd7 (update Attendance logic and fix some bugs)
