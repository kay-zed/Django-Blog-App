from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path("", views.index, name='index'),
    path("login/", login, {'template_name' : 'blog/login.html'}, name='login'),
    path("sign_up/", views.sign_up, name='sign_up'),
    path('logout/', views.log_out, name='logout'),
    path("new_post/", views.new_post, name='new_post'),
    path("<slug:slug>/", views.blog_post, name='blog_post'),

]
