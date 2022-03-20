from django.db import models


class Airport(models.Model):
    Id = models.CharField(primary_key=True, max_length=12, unique=True)
    type = models.CharField(blank=True, null=True, max_length=225)
    name = models.CharField(max_length=225)
    latitude_deg = models.DecimalField(max_digits=12, decimal_places=9)
    longitude_deg = models.DecimalField(max_digits=12, decimal_places=9)
    gps_code = models.CharField(blank=True, null=True, max_length=6)
    iata_code = models.CharField(blank=True, null=True, max_length=4)
