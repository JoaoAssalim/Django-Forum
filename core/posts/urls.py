from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('make_post/', views.make_post, name='make_post'),
    path('like-post/<int:post_id>/', views.like_post, name='like-post'),
]