from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('', views.CreateAttendanceView, name='home'),
    path('start/', views.startAttendanceView, name='start'),
<<<<<<< HEAD
    path('result/<int:id>', views.resultView, name='result'),
    path('resultlist/', views.AttendanceListView.as_view(), name='result_list'),
=======
    path('resultlist/', views.AttendanceListView.as_view(), name='result_list'),
    path('result/<int:id>/', views.resultView, name='result'),
>>>>>>> 15a2cd7 (update Attendance logic and fix some bugs)

]