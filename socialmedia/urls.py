from django.contrib import admin
from django.urls import path, include

app_name = "tle"


urlpatterns = [
    path('', include('core.home.urls')),
    path('posts/', include('core.posts.urls')),
    path('user/', include('core.login.urls')),
    path('admin/', admin.site.urls),
]