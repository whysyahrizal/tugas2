from django.db import models

from django.db import models

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    progress = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

