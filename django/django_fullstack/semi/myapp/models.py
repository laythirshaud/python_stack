from django.db import models
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Blog name should be at least 2 characters"
        if len(postData['network']) < 2:
            errors["network"] = "Blog description should be at least 2 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors



class Shows (models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    relasedate = models.CharField(max_length=255)
    desc=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager() 

