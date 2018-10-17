from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('students', views.allStudents, name='students'),
  path('students/<int:mnr>', views.oneStudent, name='student'),
]