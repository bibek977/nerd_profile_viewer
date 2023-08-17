from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


def api_home(request):

    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    # json_data = JSONRenderer().render(serializer.data)

    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data, safe=False)

# def data_by_name(request,name):

#     movie = Movie.objects.get(title=name)
#     serializer = MovieSerializer(movie)
#     json_data = JSONRenderer().render(serializer.data)

#     return HttpResponse(json_data,content_type='application/json')

def data_by_id(request,pk):

    movie = Movie.objects.get(id=pk)
    serializer = MovieSerializer(movie)
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type="application/json")