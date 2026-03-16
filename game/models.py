from django.db import models

# Create your models here.


class Game(models.Model):
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=50)
  year = models.PositiveIntegerField()
  rate = models.FloatField()
  is_free = models.BooleanField(default=True)
  
  def __str__(self):
    return f'{self.title} ({self.year})'
