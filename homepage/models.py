from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.
class User(AbstractUser):
    pass

class BlogPostManager(models.Manager):
    def unpublished (self):
        return self.get_queryset().filter(published=False)

    def published (self):
        return self.get_queryset().filter(published=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=250, null=False)
    content = RichTextField()
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = BlogPostManager()