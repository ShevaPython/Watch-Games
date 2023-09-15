from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/blog-list.html', {'posts': posts})


def post_detail(requests, pk):

    post = get_object_or_404(Post, pk=pk, status=Post.Status.PUBLISHED)

    return render(requests, 'blog/blog-detail.html',{'post':post})
