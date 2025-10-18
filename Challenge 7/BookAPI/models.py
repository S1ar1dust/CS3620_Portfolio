from django.db import models

# Create your models here.
class BookData(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name, self.category, self.description, self.rating, self.image