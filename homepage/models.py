from django.db import models

# Create your models here.
class User(models.Model):
    pass

class BlogPost(models.Model):
    title = models.CharField(max_length=250, null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)