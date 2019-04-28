"""blog_bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path

from blog import views
from blog.views import hello_world
from blog_bootcamp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('categories/', views.categories),
    path('get_category/<int:pk>', views.get_category),
    path('news/', views.news),
    path('get_news/<int:pk>', views.get_news)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)