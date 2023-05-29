from django.contrib import admin
from django.urls import path, include

app_name = "mango"


urlpatterns = [
    path('', include('core.home.urls')),
    path('posts/', include('core.posts.urls')),
    path('chat/', include('core.chat.urls')),
    path('user/', include('core.login.urls')),
    path('admin/', admin.site.urls),
]