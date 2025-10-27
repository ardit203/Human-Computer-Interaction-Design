from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='properties/', null=True, blank=True)
    reserved = models.BooleanField(null=True, blank=True)
    sold = models.BooleanField(null=True, blank=True)
    feature = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.area}'


class Agent(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    contact_phone = models.CharField(max_length=100, null=True, blank=True)
    linked_in_profile = models.CharField(max_length=100, null=True, blank=True)
    completed_sales = models.IntegerField(default=0, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class PropertyAgent(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.property} -- {self.agent}'


class Feature(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.value}'


class PropertyFeature(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.property} -- {self.feature}'
