from django.db import models
from vote.models import VoteModel

# Create your models here.


class Human(VoteModel, models.Model):
   login = models.CharField(max_length=30, unique=True)
   img = models.ImageField(default='default.jpg',upload_to='user_images')
   score = models.IntegerField(default=0)

   def __str__(self):
      return self.login




   