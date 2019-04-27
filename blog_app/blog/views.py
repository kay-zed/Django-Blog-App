from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogTopic, BlogEntry, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BlogEntryForm, BlogTopicForm, CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # get the related entry for each topic list -- to be iterated over in the template
    topic_list = BlogTopic.objects.order_by('-id').prefetch_related('blogentries')
    paginator = Paginator(topic_list, 4)
    # owner = BlogTopic.objects.filter(owner=request.user)

    page = request.GET.get('page')
    topics = paginator.get_page(page)

    context = {'topics' : topics }
    return render(request, "blog/index.html", context)


def blog_post(request, slug):
    # owner = BlogTopic.objects.filter(owner=request.user)
    title = BlogTopic.objects.get(slug=slug)
    blog_text = title.blogentries.order_by('id')
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

@login_required
def new_post(request):
    if request.method == 'POST':
        title = BlogTopicForm(request.POST)
        body = BlogEntryForm(request.POST)

        if title.is_valid() and body.is_valid():
            blog_title = request.POST.get('title')
            blog_body = request.POST.get('body')
            post_title = BlogTopic.objects.create(title=blog_title)
            post_title.save()
            post_body = BlogEntry.objects.create(title=post_title, body=blog_body)
            post_body.save()
            return HttpResponseRedirect(reverse('blog:index'))
    else:
        title = BlogTopicForm()
        body = BlogEntryForm()

    context = {'title_form' : title, 'entry_form' : body}
    return render(request, 'blog/new_post.html', context)

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))

def sign_up(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('blog:index'))

    context = {'form' : form}
    return render(request, 'blog/sign_up.html', context)            