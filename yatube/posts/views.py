from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POSTS_FILTER: int = 10

def index(request):
    posts = Post.objects.all()[:POSTS_FILTER]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
