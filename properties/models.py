from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.CharField(max_length=10)
    location = models.JSONField(null=True, blank=True)
    area = models.JSONField(null=True, blank=True)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    propertyType = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    amenities = models.JSONField()
    agent = models.JSONField()
    dateListed = models.DateTimeField(blank=True, null=True)
    images = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
