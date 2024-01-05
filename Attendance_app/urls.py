from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('', views.CreateAttendanceView, name='home'),
    path('start/', views.startAttendanceView, name='start'),
    path('result/<int:id>', views.resultView, name='result'),
    path('resultlist/', views.AttendanceListView.as_view(), name='result_list'),

]