from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

def home(request):

    intern_all = Intern.objects.all()
    
    serializer_all = InternSerializer(intern_all, many=True)

    return JsonResponse(serializer_all.data, safe=False)

def get_intern(request, pk):
    intern = Intern.objects.get(id = pk)
    serializer = InternSerializer(intern)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

def post_intern(request):
    if request.method == "POST":
        pass