from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    file = models.FileField()
    college = models.TextField()


class Car(models.Model):
    name = models.CharField(max_length=500)
    speed = models.IntegerField()

    def __str__(self) -> str:
        return self.name + "(" + str(self.speed) + ")"
