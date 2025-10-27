from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    owner = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    car_type = models.CharField(max_length=100, null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    max_speed = models.FloatField(null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.car_type}'


class Workshop(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    repairs_old_timers = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name


class Repair(models.Model):
    code = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    problem_description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='repairs/', null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code} - {self.date}'


class WorkshopManufacturer(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
