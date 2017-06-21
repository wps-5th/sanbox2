from django.conf.urls import url

from . import views

app_name = 'post'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<post_pk>\d+)/delete', views.post_delete, name='post_delete'),
    url(r'^(?P<post_pk>\d+)/detail', views.post_detail, name='post_detail'),
]
