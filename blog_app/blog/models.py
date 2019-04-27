from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class BlogTopic(models.Model):
    title = models.CharField(max_length=500)
    time_stamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(BlogTopic, self).save(*args, **kwargs) # Call the real save() method
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/{slug}".format(slug=self.slug)

class BlogEntry(models.Model):
    title = models.ForeignKey(BlogTopic, on_delete=models.CASCADE, related_name='blogentries')
    body = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'BlogEntries'
    
    def __str__(self):
            return self.body

class Comment(models.Model):
    title = models.ForeignKey(BlogTopic, on_delete=models.CASCADE)
    added_by = models.CharField(max_length=200)
    text = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.comment

