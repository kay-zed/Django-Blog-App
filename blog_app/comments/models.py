from django.db import models
from blog.models import BlogTopic

# Create your models here.
class Comment(models.Model):
    topic = models.ForeignKey(BlogTopic, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=400)
    email = models.EmailField()
    text = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text