from django.urls import path
from .views import *

urlpatterns = [
    path('', RedirectFeedView.as_view(), name='redirect_feed'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('page-404/', page_404, name='page_404'),
]