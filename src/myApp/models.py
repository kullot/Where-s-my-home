from django.db import models

class N_apartment(models.Model):
    apartment_name = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    household = models.CharField(max_length=100)
    dong = models.CharField(max_length=100)
    flat = models.CharField(max_length=100)
    d_price = models.CharField(max_length=100)
    c_price = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    i_url = models.CharField(max_length=100)
    area =  models.CharField(max_length=100)
    floor = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    day = models.CharField(max_length=100)

    def __str__(self):
        return self.apartment_name