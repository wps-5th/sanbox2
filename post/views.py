from django.shortcuts import render, redirect

# Create your views here.
from post.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)


def post_delete(request, post_pk):
    if request.method == 'POST':
        form = Post.objects.get(pk=post_pk)
        form.delete()
        return redirect('post:post_list')


def post_detail(request, post_pk):
    posts = Post.objects.get(pk=post_pk)
    context = {
        'post': posts,
    }
    return render(request, 'post_detail.html', context)
