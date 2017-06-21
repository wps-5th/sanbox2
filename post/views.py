from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

User=get_user_model()

def post_list(request):
    return HttpResponse('test')