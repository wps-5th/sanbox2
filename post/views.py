from django.shortcuts import render, redirect

# Create your views here.
from .models import Post


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
    try:
        post = Post.objects.get(pk=post_pk)

    except Post.DoesNotExist as e:
        return redirect('post:post_list')

    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)
