from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    progress = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

