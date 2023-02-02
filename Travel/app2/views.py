from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.

def home(request):
    obj1 = models.Travel.objects.all()
    obj2 = models.Team.objects.all()

    return render(request, 'index.html', {'place': obj1, 'team': obj2})

# def calculate(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x + y
#     sub = x - y
#     mul = x * y
#     div = x / y
#     return render(request, 'result.html',
#                   {'num1': x, 'num2': y, 'addition': add, 'subtraction': sub, 'multiplication': mul, 'division': div})

#
#
#
# def details(request):
#     return HttpResponse('This is Detail Page')
#
#
# def thanks(request):
#     return HttpResponse('Thanks')
