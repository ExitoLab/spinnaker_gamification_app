from django.db import models

# Create your models here.

class issue(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    number = models.CharField(max_length=50)
    date_created_at = models.DateTimeField(auto_now_add=True)
    date_updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class issue_user(models.Model):
    login = models.TextField()
    type = models.TextField()
    number = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.login

class record_last_number(models.Model):
    last_issue_number = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.last_issue_number

# Add model for comments

class comment(models.Model):
    github_id = models.IntegerField()
    github_number = models.TextField()
    login = models.TextField()
    url = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    date_created_at = models.DateTimeField(auto_now_add=True)
    date_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
