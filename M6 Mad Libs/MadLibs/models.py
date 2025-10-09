from django.db import models



class Input(models.Model):
    name = models.CharField(max_length=150)
    noun1 = models.CharField(max_length=100)
    noun2 = models.CharField(max_length=100)
    place = models.CharField(max_length=150)
    verb = models.CharField(max_length=100)
    adjective = models.CharField(max_length=100)
    person = models.CharField(max_length=150)

    def __str__(self):
        return self.name, self.noun1, self.noun2, self.place, self.verb, self.adjective, self.person


class Story(models.Model):
    tellStory = models.TextField()

    def __str__(self):
        return self.tellStory