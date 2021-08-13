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
    title_slug = models.SlugField(primary_key=True, unique=True, max_length=50)
    content = RichTextField()
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = BlogPostManager()

class PortfolioProject(models.Model):
    title = models.CharField(max_length=250, null=False)
    title_slug = models.SlugField(primary_key=True, unique=True, max_length=50)
    description = RichTextField()
    ongoing = models.BooleanField(default=False)
    main_image = models.ImageField()