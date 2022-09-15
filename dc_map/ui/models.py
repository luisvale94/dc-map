from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Datacenter(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    lat = models.FloatField()
    lng = models.FloatField()

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
