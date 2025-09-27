from django.db import models
from django.contrib import admin
class car(models.Model):
    car = models.CharField(max_length=255)
    model = models.CharField(max_length=100)
    manufacture_date = models.DateField
    type = models.CharField(max_length=50)
    price = models.IntegerField

class carAdmin(admin.ModelAdmin):
    list_display = ('car', 'model', 'manufacture_date', 'type', 'price')

# Create your models here.
