from django.db import models

class Flight(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    flightTypes = [
        ("NTL", "Nacional"),
        ("INTL", "Internacional"),
    ]

    flight_type = models.CharField(max_length=4, choices = flightTypes)
