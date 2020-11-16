from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


# api for ajax
from myapp.models import TestModel


def list_view(request):
    models = TestModel.objects.all()
    return JsonResponse({'models': models})


def create_view(request):
    model = TestModel()
    if request.POST:
        data = request.POST.get('data')
        model.name = data.name
        model.date = data.date
        model.age = data.age
        model.save()


def update_view(request):
    pass


def delete_view(request):
    pass
