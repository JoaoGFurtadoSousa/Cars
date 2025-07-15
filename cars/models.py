from django.db import models

# Create your models here.

BRANDS = (
    ('CHEVROLET','CHEVROLET'),
    ('FORD','FORD'),
    ('NISSAN','NISSAN'),
    ('CITROEN','CITROEN')
)

class Cars(models.Model):
    model = models.CharField(max_length=50)
    brand = models.CharField(choices= BRANDS, max_length=20)
    year = models.IntegerField()


    def __str__(self):
       return self.model 

