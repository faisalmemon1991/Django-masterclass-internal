from django.contrib import admin

from blogapp.models import Category, Comments, Post, Profile, Tag, WebsiteMeta

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# class ProfileAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("user.username",)}

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comments)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(WebsiteMeta)