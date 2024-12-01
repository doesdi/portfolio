from django.conf.urls import handler404
from django.contrib import admin
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, include
from main import views
from main.views import *
from portfolio import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound