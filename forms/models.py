from django.db import models

# Create your models here.

class CustomUser(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Email = models.EmailField()
    Message = models.TextField()
    Video = models.FileField(upload_to='uploads/')