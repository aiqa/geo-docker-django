from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    population = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
