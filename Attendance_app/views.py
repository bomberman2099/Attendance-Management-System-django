from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
<<<<<<< HEAD
<<<<<<< HEAD
=======
from django.views.generic import TemplateView

>>>>>>> 15a2cd7 (update Attendance logic and fix some bugs)
=======
>>>>>>> origin/main
from . import models
from datetime import datetime, timezone, timedelta
from django.views.generic.list import ListView
from .models import AttendanceUser
from .mixin import CustomizedRquirementLogin

<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 15a2cd7 (update Attendance logic and fix some bugs)
=======
>>>>>>> origin/main
class AttendanceListView(CustomizedRquirementLogin, ListView):
    model = AttendanceUser
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = AttendanceUser.objects.filter(user=self.request.user)
        return context
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
def CreateAttendanceView(request):
    if not request.user.is_authenticated:
        return reverse("user:login")

    return render(request, 'Attendance_app/index.html', {})
<<<<<<< HEAD
=======


def CreateAttendanceView(request):
    if request.user.is_anonymous:
        return reverse("user:login")
    return render(request, 'Attendance_app/index.html')
>>>>>>> 15a2cd7 (update Attendance logic and fix some bugs)
=======
>>>>>>> origin/main


def startAttendanceView(request):
    if not request.user.is_authenticated:
        return reverse("user:login")

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
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

<<<<<<< HEAD
=======
    start = datetime.now().time()
    date = datetime.now().date()
    try:
        at = AttendanceUser.objects.get(user=request.user, end=None)
        return render(request, 'Attendance_app/start.html', {'started': at.start, 'pk': at.id})
    except AttendanceUser.DoesNotExist:
        try:
            at = AttendanceUser.objects.get(user=request.user, created_date=date)
            at.start = start
            at.end = None
            at.save()
            return render(request, 'Attendance_app/start.html', {'started': start, 'pk': at.id})
        except AttendanceUser.DoesNotExist:
            at = AttendanceUser.objects.create(user=request.user, created_date=date, start=start,)
            at.end = None
            at.save()
            return render(request, 'Attendance_app/start.html', {'started': start, 'pk': at.id})
>>>>>>> 15a2cd7 (update Attendance logic and fix some bugs)
=======
>>>>>>> origin/main


def resultView(request, id):
    if not request.user.is_authenticated:
        return reverse("user:login")

    attend = get_object_or_404(AttendanceUser, user=request.user, id=id)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
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
<<<<<<< HEAD
=======
    if attend.end is not None:
        return redirect("home:result_list")
    end = datetime.now().time()
    attend.end = end

    job_time = datetime.combine(datetime.min, attend.end) - datetime.combine(datetime.min, attend.start)
    attend.job_time = job_time

    attend.save()
    attend.end = None

    end_datetime = datetime.combine(datetime.today(), end)
    start_datetime = datetime.combine(datetime.today(), attend.start)

    # Format the datetime objects
    end = end_datetime.strftime("%I:%M:%S %p")
    start = start_datetime.strftime("%I:%M:%S %p")

    return render(request, 'Attendance_app/result.html', {'attend': attend, "end": end, "start": start})

>>>>>>> 15a2cd7 (update Attendance logic and fix some bugs)
=======
>>>>>>> origin/main

