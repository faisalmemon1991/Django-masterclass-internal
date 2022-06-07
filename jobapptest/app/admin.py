from django.contrib import admin

from app.models import Author, JobPost, Location

class LocationAdmin(admin.ModelAdmin):
    pass

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title', 'date', 'salary')
    list_filter = ('date', 'salary','expiry')
    search_fields= ['title','description']
    search_help_text = "Write in your query and hit enter"
    # fields = (("title", "description"),"expiry")
    # exclude = ("title")
    fieldsets = (
        ("Basic information", {
            'fields': ('title', 'description')
        }),
        ('More information', {
            'classes': ('collapse',),
            'fields': (('expiry', 'salary'), 'slug'),
        }),
        )

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location, LocationAdmin)
admin.site.register(Author)