from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_feed, name='redirect_feed'),
    path('feed/', views.feed, name='feed'),
]