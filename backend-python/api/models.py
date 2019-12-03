from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    population = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Mountain(models.Model):
    name = models.CharField(max_length=255)
    height = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class River(models.Model):
    name = models.CharField(max_length=255)
    length = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
