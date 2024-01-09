from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import reverse
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
    if request.user.is_anonymous:
        return redirect(reverse("user:login"))
    return render(request, 'Attendance_app/index.html')


def startAttendanceView(request):
    if not request.user.is_authenticated:
        return reverse("user:login")

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



def resultView(request, id):
    if not request.user.is_authenticated:
        return reverse("user:login")

    attend = get_object_or_404(AttendanceUser, user=request.user, id=id)
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


