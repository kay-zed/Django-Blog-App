from django.shortcuts import render
from .models import Comment

# Create your views here.
def comment(request):
    comments = Comment.objects.filter(topic=title).order_by("-id")

    if request.method == 'POST':
        # create blank comment form
        form = CommentForm(request.POST or None)
        if form.is_valid():
            text = request.POST.get('text')
            email = request.POST.get('email')
            name = request.POST.get('name')
            time_stamp = request.POST.get('time_stamp')
            comment = Comment.objects.create(topic=title, text=text, email=email, 
                                                time_stamp=time_stamp, name=name)
            comment.save()
            return HttpResponseRedirect(title.get_absolute_url())
    
    else:
        form = CommentForm()
