from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
        fullname = models.CharField(max_length=50)
        email = models.EmailField()
        message = models.TextField()

        def __str__(self):
                return self.fullname + self.message


