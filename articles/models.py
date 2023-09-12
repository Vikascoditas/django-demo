from django.db import models
from dataclasses import dataclass
# Create your models here.
class Article(models.Model):


    title= models.TextField()
    content=models.TextField()
