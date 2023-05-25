from django.contrib import admin
from django.urls import path, include

app_name = "mango"

urlpatterns = [
    path('', include('core.login.urls')),
    path('dash/', include('core.home.urls')),
    path('dash/', include('core.posts.urls')),
    path('dash/', include('core.chat.urls')),
    path('admin/', admin.site.urls),
]

handler403 = 'core.http_codes.views.handler403'
handler404 = 'core.http_codes.views.handler404'
handler500 = 'core.http_codes.views.handler500'