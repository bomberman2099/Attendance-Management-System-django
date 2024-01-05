from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from . import models
from datetime import datetime, timezone, timedelta
from django.views.generic.list import ListView
from .models import AttendanceUser
from .mixin import CustomizedRquirementLogin

class AttendanceListView(CustomizedRquirementLogin, ListView):
    model = AttendanceUser
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = AttendanceUser.objects.filter(user=self.request.user)
        return context
def CreateAttendanceView(request):
    if not request.user.is_authenticated:
        return reverse("user:login")

    return render(request, 'Attendance_app/index.html', {})


def startAttendanceView(request):
    if not request.user.is_authenticated:
        return reverse("user:login")

    start = datetime.now()
    date = datetime.now().date()
    try:
        at = AttendanceUser.objects.get(user=request.user, created_date=date,)
        at.start = start
        at.save()
        return render(request, 'Attendance_app/start.html', {'started': start, 'pk': at.id})
    except ObjectDoesNotExist:
        at = AttendanceUser.objects.create(user=request.user, created_date=date, start=start)
        return render(request, 'Attendance_app/start.html', {'started': start, 'pk': at.id})



def resultView(request, id):
    if not request.user.is_authenticated:
        return reverse("user:login")

    attend = get_object_or_404(AttendanceUser, user=request.user, id=id)
    attend.save()
    # print(attend.end, attend.start)
    job_time = datetime.combine(datetime.min, attend.end) - datetime.combine(datetime.min, attend.start)
    hours = job_time.seconds // 3600
    minutes = (job_time.seconds // 60) % 60
    seconds = job_time.seconds % 60

    if attend.job_time:
        existing_job_time = datetime.strptime(str(attend.job_time), "%H:%M:%S")
        total_job_time = existing_job_time + timedelta(hours=hours, minutes=minutes, seconds=seconds)
        attend.job_time = total_job_time.strftime("%H:%M:%S")
    else:
        attend.job_time = f"{hours}:{minutes:02d}:{seconds:02d}"

    attend.user = request.user
    attend.save()
    # print(attend.end, attend.start)
    return render(request, 'Attendance_app/result.html', {'attend': attend})

