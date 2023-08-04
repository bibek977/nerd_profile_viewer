from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profiles/')
    email = models.EmailField(max_length=100)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=200, default="Out of Valley")

    def __str__(self):
        return self.name
    
class Geeks_Model(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    roll = models.PositiveIntegerField()
    author = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title