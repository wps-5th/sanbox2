from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from post.foms.post import PostForm
from .models import Post

User = get_user_model()


# def post_list(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'post/post_list.html', context)


def post_list(request):
    post = Post.objects.all().order_by('created_date')
    context = {
        'posts' : post,
        'post_form' : PostForm(),
    }
    return render(request, 'post/post_list.html', context)

@require_POST
def post_delete(request, post_pk):

    form = Post.objects.get(pk=post_pk)
    print(form)
    form.delete()
    print(form)
    return redirect('post:post_list')


def post_detail(request, post_pk):
    try:
        post = Post.objects.get(pk=post_pk)

    except Post.DoesNotExist as e:
        return redirect('post:post_list')

    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        user = User.objects.first()
        post = Post.objects.create(
            author=user,
            photo=request.FILES['file'],
        )
        comment_string = request.POST.get('comment','')
        if comment_string:
            post.comment_set.create(
                author=user,
                content=comment_string,
            )
            return redirect('post:post_detail', post_pk=post.pk)
        else:
            return render(request, 'post/post_create.html')
    return render(request,'post/post_create.html')

