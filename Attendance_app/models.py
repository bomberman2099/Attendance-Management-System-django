from datetime import datetime, timedelta
from datetime import timezone
from django.contrib.auth.models import User
from django.db import models

class AttendanceUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
<<<<<<< HEAD
    created_date = models.DateField(auto_now_add=True)
    start = models.TimeField(auto_now_add=True, blank=True)
    end = models.TimeField(auto_now=True, null=True, blank=True)
    job_time = models.TimeField(null=True, blank=True, default=None)
=======
    created_date = models.DateField(auto_now=False, null=True)
    start = models.TimeField(auto_now=False, null=True, blank=True)
    end = models.TimeField(auto_now=False, null=True, blank=True)
    job_time = models.DurationField(null=True, blank=True)


>>>>>>> 15a2cd7 (update Attendance logic and fix some bugs)




