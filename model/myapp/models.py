from django.db import models

from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

class Car(models.Model):
    
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
    model_name = models.CharField(max_length=50)
