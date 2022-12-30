from django.urls import  path
from . import views

urlpatterns=[
    
    path('student', views.studentListCreate.as_view()),
    path('employee', views.employeeListCreate.as_view()),
    path('teacher', views.teacherListCreate.as_view()),
    path('student/update/<int:pk>',views.studentUpdate.as_view()),
    path('employee/update/<int:pk>', views.employeeUpdate.as_view()),
    path('teacher/update/<pk>', views.teacherUpdate.as_view()),
]