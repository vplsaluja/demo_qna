from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class QuestionModel(models.Model):
    owner = models.ForeignKey('auth.User', related_name='question', on_delete=models.CASCADE)

    quest_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
