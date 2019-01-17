from django.db import models

# Create your models here.
class user(models.Model):
    no = models.IntegerField(default=0)     #编号
    gender = models.BooleanField(default=False) #默认为Male(False)
    bmi = models.FloatField(default=0)
    age = models.IntegerField(default=0)
    insulin = models.IntegerField(default=0)
    func = models.FloatField(default=0)
    blood_sugar = models.FloatField(default=0)
    ifpreg = models.BooleanField(default=False)
    pregancy = models.IntegerField(default=0)
    blood_pressure = models.FloatField(default=0)
    skin_thickness = models.FloatField(default=0)
    result = models.BooleanField(default=False)

