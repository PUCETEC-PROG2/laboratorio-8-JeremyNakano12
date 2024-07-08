from django.db import models

# Create your models here.

class Pokemon (models.Model):
    name = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=15, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    
    def __str__(self) -> str:
        return self.name
    
class Trainer (models.Model):
    name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)
    level = models.IntegerField(null=False)
    region = models.CharField(max_length=30, null=True)
    
    def __str__(self) -> str:
        return self.name