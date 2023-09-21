from django.db import models

from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10)
    theory_hours = models.IntegerField()
    semester = models.IntegerField()
    practical_hours = models.IntegerField()