from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class FoodType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Food(models.Model):
    foodType = models.ForeignKey(FoodType, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='food/')
    cal = models.IntegerField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=CASCADE)
    img = models.ImageField(upload_to='article/')
    intro = models.TextField()
    detail = models.TextField()

    def __str__(self):
        return self.title
    