from django.db import models

# Create your models here.
'''
Поля Бетона: марка-строка, морозостойкость-строка, водонепроницаемость-строка,
подвижность-строка, цена-десимал
 
'''

class Beton(models.Model):
    name = models.CharField(max_length=100)
    frost_resistance = models.CharField(max_length=10)
    water_resistance = models.CharField(max_length=10)
    mobility = models.CharField(max_length=10)
    price = models.FloatField()


    def __str__(self):
        return self.name