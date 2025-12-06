from django.db import models

# Create your models here.
class Villagers(models.Model):
    name = models.CharField(max_length=50 , primary_key=True, unique=True)
    species = models.CharField(max_length=50)
    birthday = models.DateField()#input_formats=['%m/%Y'])
    gender = models.CharField(max_length=1)
    personality = models.CharField(max_length=50)
    initialCatchphrase = models.CharField(max_length=50)
    skill = models.CharField(max_length=50)
    goal = models.CharField(max_length=100)
    image = models.ImageField()#upload_to='static/Images/')

    @property
    def return_image_url(self):
        return f"Images/{self.image.name}"

    def __str__(self):
        return self.name, self.species, self.birthday, self.gender, self.personality,  self.initialCatchphrase, self.skill, self.goal, self.image

class Messages(models.Model):
    name = models.CharField(max_length=50)    #ForeignKey(Villagers, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.name, self.message

class Posts(models.Model):
    image = models.ImageField()#upload_to='static/Images/')
    name = models.CharField(max_length=50)
    personality = models.CharField(max_length=50)
    message = models.TextField()

    @property
    def return_image_url(self):
        return f"Images/{self.image.name}"

    def __str__(self):
        return self.image, self.name, self.personality, self.message
