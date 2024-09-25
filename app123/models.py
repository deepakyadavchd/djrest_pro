from django.db import models


class Car(models.Model):
    brandname=models.CharField(max_length=100)
    brandmodel=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    milage=models.CharField(max_length=100)
    perdayrent=models.IntegerField()

    def __str__(self):
        return self.brandname

