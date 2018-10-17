from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def studentss(request):
    students = Student.objects.all().values() # or simply .values() to get all fields
    students_list = list(students)  # important: convert the QuerySet to a list object
    return HttpResponse(students_list)
