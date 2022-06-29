from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Post(models.Model):
    title=models.CharField(max_length=200)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now= True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='post_tags')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    view_count = models.IntegerField(null=True, blank=True)
    like_count = models.IntegerField(null=True, blank=True)

    def save(self, *args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

class Comments(models.Model):
    title=models.CharField(max_length=200)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete= models.CASCADE)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)
