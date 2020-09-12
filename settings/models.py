from django.db import models

# Create your models here.

class GithubDetails(models.Model):
    title = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    token = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title