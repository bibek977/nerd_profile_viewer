from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    actress = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    runtime = models.IntegerField()
    imdb = models.FloatField()
    summary = models.TextField()

    def __str__(self):
        return self.title