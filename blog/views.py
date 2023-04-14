from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

def post_list(request):
    """Displays the list of posts"""

    posts = Post.published.all()
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})


def post_detail(request, id):
    """Display single post or 404 error if post is not found."""

    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
    