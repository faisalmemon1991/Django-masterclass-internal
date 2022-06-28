from django.contrib import admin

from blogapp.models import Bookmark, Category, Comments, Post, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Bookmark)