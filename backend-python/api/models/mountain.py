from django.db import models


class Mountain(models.Model):
    name = models.CharField(max_length=255)
    height = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
