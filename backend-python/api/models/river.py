from django.db import models


class River(models.Model):
    name = models.CharField(max_length=255)
    length = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
