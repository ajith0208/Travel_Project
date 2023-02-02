from django.db import models


# Create your models here.

class Travel(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.name

class movie(models.Model):
    movie_name = models.CharField(max_length=250)
    cost = models.IntegerField()
    director = models.TextField()
    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.movie_name
