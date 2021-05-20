from django.db import models
    
class user(models.Model):
    first_name = models.CharField(max_length=45)
    secand_name = models.CharField(max_length=45)
    email_address= models.TextField()

    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
