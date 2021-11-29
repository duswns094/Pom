from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='project/', null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now=True, null=True)