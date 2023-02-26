from django.db import models

# Create your models here.

class User(models.Model):
    namex =models.CharField(max_length=30)
    created_at =models.DateTimeField(auto_now_add=True, null=True)
    updated_at =models.DateTimeField(auto_now=True)
    
class Post(models.Model):
    content = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True, null=True)
    updated_at =models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True, null=True)
    updated_at =models.DateTimeField(auto_now=True)
    

    