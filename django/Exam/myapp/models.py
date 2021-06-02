from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Thought(models.Model):
    description = models.TextField()
    uploade_by=models.ForeignKey(User, related_name="uploaded", on_delete=models.CASCADE)
    liked_by=models.ManyToManyField(User, related_name="like")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)