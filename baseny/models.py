from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Basen(models.Model):
    VOIVODESHIP = [
            ('DS', 'Dolnośląskie'),
            ('KP', 'Kujawsko-Pomorskie'),
            ('LU', 'Lubelskie'),
            ('LB', 'Lubuskie'),
            ('LD', 'Łódzkie'),
            ('MA', 'Małopolskie'),
            ('MZ', 'Mazowieckie'),
            ('OP', 'Opolskie'),
            ('PK', 'Podkarpackie'),
            ('PD', 'Podlaskie'),
            ('PM', 'Pomorskie'),
            ('SL', 'Śląskie'),
            ('SK', 'Świętokrzyskie'),
            ('WN', 'Warmińsko-mazurskie'),
            ('WP', 'Wielkopolskie'),
            ('ZP', 'Zachodniopomorskie')]
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)  # official name of pool
    www = models.CharField(max_length=100)  # www address (URL)
    details = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    # geo = models.CharField(max_length=30)
    # make it with validation if in Poland:
    #     lat (49, 54.85), lon (14.07, 24.2) (precision good enough)
    lat = models.FloatField(validators=[MinValueValidator(0),
                                        MaxValueValidator(90)],
                            default=52.0689883)
    lon = models.FloatField(validators=[MinValueValidator(-180),
                                        MaxValueValidator(180)],
                            default=19.4799726)

    voivodeship = models.CharField(max_length=2, choices=VOIVODESHIP)
    remarks = models.CharField(max_length=100)

    
    def __str__(self):
        return f"city={self.city}, name={self.name}"
