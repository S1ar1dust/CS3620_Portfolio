from django.db import models


class Hobby(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name, self.description

class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name, self.description

