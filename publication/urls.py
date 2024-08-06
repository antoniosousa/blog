from .views import index, post
from django.urls import path 

urlpatterns = [
    path('', index, name='index'),
    path('post/1/', post, name='post'),
]
