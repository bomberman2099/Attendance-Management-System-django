from django.contrib import admin
from .models import AttendanceUser

class AttendanceUserAdmin(admin.ModelAdmin):
    fields = ('user', 'created_date', 'start', 'end', 'job_time')


admin.site.register(AttendanceUser, AttendanceUserAdmin)

