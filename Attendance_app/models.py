from datetime import datetime, timedelta
from datetime import timezone
from django.contrib.auth.models import User
from django.db import models

class AttendanceUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_date = models.DateField(auto_now=False, null=True)
    start = models.TimeField(auto_now=False, null=True, blank=True)
    end = models.TimeField(auto_now=False, null=True, blank=True)
    job_time = models.DurationField(default=timedelta(0), blank=True)







