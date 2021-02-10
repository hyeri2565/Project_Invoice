from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class model1(models.Model):
    title=models.CharField(max_length=100,primary_key=True)
    date=models.DateTimeField()

class User(AbstractUser):
    company_id=models.CharField(max_length=10)
    companyCellular=models.CharField(max_length=11)

'''model 2가지 필요 ->
-회원들의 정보를 담을 User모델
-운송장 정보를 담을 invoice모델'''