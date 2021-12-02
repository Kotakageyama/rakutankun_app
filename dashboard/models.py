from django.db import models
from django.conf import settings
from django.utils import timezone

class User(models.Model):
    student_id = models.CharField(max_length=10, blank=False)
    passwd = models.CharField(blank=False,max_length=30)
    username = models.CharField(max_length=20, default='名称未設定')
    credits_list = models.CharField(default='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',max_length=1000)

class CreditsData(models.Model):
    Number = models.IntegerField()
    ClassName = models.CharField(max_length=20,default=None)
    CreditScore = models.IntegerField()
    CreditCondition = models.IntegerField()
    CompulsoryFlag = models.IntegerField()
