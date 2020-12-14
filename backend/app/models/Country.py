from django.db import models


class CountryORM(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name