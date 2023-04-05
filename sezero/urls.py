"""sezero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from tech import views
from django.contrib import admin
from django.urls import path
from tech.views import home,postdetail,uploadi,uploadf,upload_link_view,editpost, landing, projects, blog_home
from django.views.decorators.csrf import csrf_exempt 

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing),
    path('dezolver/', views.scrape),
    path('accounts/', include('allauth.urls')),
    path('blog/',blog_home),
    path('blog/write/',home ),
    path('blog/<int:id>/',postdetail ),
    path('blog/edit/<str:title>/',editpost ),
    path('uploadi/',csrf_exempt(uploadi) ),
    path('uploadf/',csrf_exempt(uploadf) ),
    path('linkfetching/',upload_link_view),
    path('projects/',projects),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    # path('social-auth/', include('social_django.urls', namespace='social')),
