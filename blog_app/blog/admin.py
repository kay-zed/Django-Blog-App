from django.contrib import admin
from .models import BlogEntry, BlogTopic, Comment
from django.utils.text import slugify

# Register your models here

@admin.register(BlogTopic)
class BlogTopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogEntry)
admin.site.register(Comment)



