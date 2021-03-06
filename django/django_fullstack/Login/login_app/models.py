
from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


# class Message(models.Model):
#     message = models.CharField(max_length=255)
#     user= models.ForeignKey(User, related_name="users", on_delete = models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
#     comment = models.CharField(max_length=255)
#     message_com= models.ForeignKey(Message, related_name="messages", on_delete = models.CASCADE)
#     user_com= models.ForeignKey(User, related_name="useer_com", on_delete = models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)