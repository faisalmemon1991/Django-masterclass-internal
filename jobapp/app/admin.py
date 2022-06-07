from django.contrib import admin

from app.models import JobPost, Location

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)