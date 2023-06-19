from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    def __str__(self):
        return self.content

    title = models.CharField(max_length=100, default='Title')
    content = models.TextField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    def __str__(self):
        return self.content

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
