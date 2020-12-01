from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from post.views import index, blog, post

urlpatterns=[
    path('admin/', admin.site.urls),
    path('blog/<id>/', blog, name='post-detail'),
    path('post/', post),
    path('', index, name='post-list'),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)