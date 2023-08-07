from django.db import models


class Intern(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    program = models.CharField(max_length=50)

    def __str__(self):
        return self.name