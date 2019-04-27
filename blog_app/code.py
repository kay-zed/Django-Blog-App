# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BlogTopic, BlogEntry, Comment

---snip---
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['added_by', 'text']


# blog/models.py
class BlogTopic(models.Model):
    ---snip---
    
    def get_absolute_url(self):
        return "/{slug}".format(slug=self.slug)

# blog/views.py
def blog_post(request, slug):
    ---snip---
    comments = Comment.objects.filter(title=title).order_by("-id")

    if request.method == 'POST':
        # create blank comment form
        form = CommentForm(request.POST or None)
        if form.is_valid():
            text = request.POST.get('text')
            name = request.POST.get('added_by')
            time_stamp = request.POST.get('time_stamp')
            comment = Comment.objects.create(title=title, text=text,
                                            time_stamp=time_stamp, added_by=name)
            comment.save()
            return HttpResponseRedirect(title.get_absolute_url())
    
    else:
        form = CommentForm()
    context = {'title' : title, 'blog_text' : blog_text, 'comments' : comments, 'form' : form} 
    return render(request, 'blog/blog_post.html', context)

