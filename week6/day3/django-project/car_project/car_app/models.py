from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=50, null=False, blank=False)
    brand_img = models.TextField(null=True, blank=True)


class Car(models.Model):
    car_name = models.CharField(max_length=50, null=False, blank=False)
    car_model = models.CharField(max_length=50, null=False, blank=False)
    car_color = models.CharField(max_length=50, null=False, blank=False)
    car_year_created = models.CharField(max_length=50, null=False, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")
    car_img = models.TextField(null=True, blank=True)
