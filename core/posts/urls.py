from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('make_post/', views.make_post, name='make_post'),
    path('make_comment/<int:id>/', views.make_comment, name='make_comment'),
    path('like-post/<int:post_id>/', views.like_post, name='like-post'),
]