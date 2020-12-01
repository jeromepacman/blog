from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Post


def index(request):
    search_post=request.GET.get('search')
    if search_post:
        featured=Post.objects.filter(
            Q(title__icontains=search_post) |
            Q(description__icontains=search_post)
        ).distinct()
    else:
        featured=Post.objects.filter(featured=True)

    latest=Post.objects.order_by('-timestamp')[0:3]
    context={'object_list': featured, 'latest': latest}
    return render(request, 'index.html', context)


def blog(request, id):
    post=get_object_or_404(Post, id=id)
    form=CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user=request.user
            form.instance.post=post
            form.save()

    return render(request, 'blog.html', {'post': post, 'form': form})


def post(request):
    return render(request, 'post.html', {})
