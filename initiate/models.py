from django.db import models

# Create your models here.
class model1(models.Model):
    title=models.CharField(max_length=100,primary_key=True)
    date=models.DateTimeField()