from django.db import models

# Create your models here.
class Student(models.Model):
    vorname = models.CharField(max_length=255, blank=False)
    nachname = models.CharField(max_length=255, blank=False)
    matrikelnummer = models.IntegerField(primary_key=True)
    studiengang = models.CharField(max_length=2, blank=False)
    semester = models.IntegerField(blank=False)
    email = models.CharField(max_length=255, blank=False)
