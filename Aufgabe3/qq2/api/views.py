import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def allStudents(request):
    if request.method == 'GET':
        students = Student.objects.all().values()
        students_list = list(students)
        return JsonResponse(students_list, safe=False)
    elif request.method == 'POST':
        json_data = json.loads(request.body)
        newStudent = Student(firstname=json_data['firstname'], lastname=json_data['lastname'], matriculation_number=json_data['matriculation_number'], course=json_data['course'], email=json_data['email'])
        newStudent.save()
        return JsonResponse(json_data)

def oneStudent(request, mnr):
    student = Student.objects.get(matriculation_number=mnr)
    if request.method == 'GET':
        return JsonResponse(student.to_dict(), safe=False)
    elif request.method == 'PATCH':
        json_data = json.loads(request.body)
        student.firstname = json_data['firstname']
        student.lastname = json_data['lastname']
        student.matriculation_number = json_data['matriculation_number']
        student.course = json_data['course']
        student.email = json_data['email']
        student.save()
        return JsonResponse(student.to_dict(), safe=False)
    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse()
