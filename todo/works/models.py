from django.db import models

# Create your models here.
class Activity(models.Model):
    content = models.CharField(max_length= 1024)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.content
