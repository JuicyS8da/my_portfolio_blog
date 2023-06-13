"""
URL configuration for portfolio_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('', cache_page(60)(index), name='index'),
    path('blog/', Blog.as_view(), name='blog'),
    path('works/', Works.as_view(), name='works'),
    path('blog/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('work/<slug:work_slug>/', ShowWork.as_view(), name='work'),
    path('blog/category/<slug:cat_slug>', ShowPostCategory.as_view(), name='post_category'),
    path('work/category/<slug:cat_slug>', ShowWorkCategory.as_view(), name='work_category'),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)