from django.test import TestCase
from .models import *
# import redgreenunittest as unittest

class AssociationTestCase(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(brand_name='Toyota')
        self.car1 = Car.objects.create(car_name='Prius', car_model='x', car_color='white', car_year_created='Sept 4, 2022', brand=self.brand)
        self.car2 = Car.objects.create(car_name='Camry', car_model='y', car_color='black', car_year_created='Sept 3 2022', brand=self.brand)
        self.car3 = Car.objects.create(car_name='Corrola', car_model='z', car_color='gray', car_year_created='Sept 2 2022', brand=self.brand)

    def test_01_brand_cars(self):
        """returns the brand's list of cars"""
        self.assertEqual(list(self.brand.cars.all()),[self.car1,self.car2,self.car3])

    def test_02_car_brand(self):
        """returns the car's brand name"""
        self.assertEqual([self.brand.brand_name], [self.car1.brand.brand_name])
