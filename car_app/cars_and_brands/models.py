from django.db import models
from django.core.exceptions import ValidationError

def car_year_validator(year):
    if year < 1800:
        raise ValidationError('Please input a car year greater than 1800')

class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField() #What Adam said when he nearly got hit by one

class Car(models.Model):
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    model= models.CharField(max_length=200)
    year= models.IntegerField(validators=[car_year_validator])
    adam_curse = models.TextField() #What Adam said when he nearly got hit by one