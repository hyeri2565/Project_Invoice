from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class model1(models.Model):
    title=models.CharField(max_length=100,primary_key=True)
    date=models.DateTimeField()

class User(AbstractUser):
    company_id=models.CharField(max_length=10)