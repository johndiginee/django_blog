from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import Http404

def post_list(request):
    """Displays the list of posts"""

    posts = Post.published.all()
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})


def post_detail(request, year, month, day, post):
    """Display single post or 404 error if post is not found."""

    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
    