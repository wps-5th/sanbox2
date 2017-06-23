from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    if request.method == 'POST':
        # return render(request, 'login.html')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            author=username,
            password=password,
        )
        if user is not None:
            django_login(request, user)
        else:
            return redirect('post:post_list')
    else:
        if request.user.is_isauthenticated:
            return redirect('post_list')
        return render(request, 'member/login.html')


def logout(request):
    if request.method == 'POST':
        django_logout(request)
        return redirect('post:post_list.html')
