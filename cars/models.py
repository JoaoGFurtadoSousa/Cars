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
    brand = models.CharField(choices= BRANDS, max_length=20, default='Chevrolet')
    year = models.IntegerField()
    image = models.ImageField(upload_to='media', null = True, blank = True)


    def __str__(self):
       return self.model 

