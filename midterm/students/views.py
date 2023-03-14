from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from students.models import Student
from students.serializers import StudentSerializer
import json


@csrf_exempt
def handle_categories(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(data=serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)

def get_student(pk):
    try:
        student = Student.objects.get(id=pk)
        return {
            'status': 200,
            'student': student
        }
    except Student.DoesNotExist as e:
        return {
            'status': 404,
            'student': None
        }


@csrf_exempt
def student_handler(request, pk):
    result = get_student(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Student not found'}, status=404)

    student = result['student']

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data, status=200)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = StudentSerializer(data=data, instance=student)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data=serializer.errors, status=400)
    if request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'Student deleted successfully!'})
    return JsonResponse({'message': 'Request is not supported'}, status=400)
