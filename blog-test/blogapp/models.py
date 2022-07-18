import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField()
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args,**kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        return super(Profile, self).save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args,**kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Tag, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args,**kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

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
    # like_count = models.IntegerField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_like', default=None, blank=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmarks", default=None, blank=True)
    is_featured = models.BooleanField()

    def save(self, *args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()

class Comments(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now= True)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    author = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200) 
    website=models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='replies')

# class Bookmark(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     posts = models.ManyToManyField(Post)

# class LikedPosts(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     posts = models.ManyToManyField(Post)


class WebsiteMeta(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    about = models.TextField()
