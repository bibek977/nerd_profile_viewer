from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    actor = serializers.CharField(max_length=100)
    actress = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    director = serializers.CharField(max_length=100)
    writer = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    year = serializers.IntegerField()
    runtime = serializers.IntegerField()
    imdb = serializers.FloatField()
    summary = serializers.CharField()