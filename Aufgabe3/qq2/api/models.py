from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=255, blank=False)
    lastname = models.CharField(max_length=255, blank=False)
    matriculation_number = models.IntegerField(primary_key=True)
    course = models.CharField(max_length=2, blank=False)
    email = models.CharField(max_length=255, blank=False)

    def to_dict(self):
        return {"firstname": self.firstname, "lastname": self.lastname, "matriculation_number": self.matriculation_number, "course": self.course, "email": self.email}
