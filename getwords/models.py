from django.db import models

# Create your models here.


class GetWord(models.Model):
   spell = models.CharField(max_length=100)