"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import re_path
from project.settings import MEDIA_ROOT
import xadmin
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from password.views import Password_list,Password_detail,Password_forms,index
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^password/$', Password_list, name='password'),
    url(r'^password/(?P<password_id>\d+)/$', Password_detail, name="detail_password"),
    url(r'^xadmin/', xadmin.site.urls, name='xadmin'),
    url(r'media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^password_form/$', Password_forms, name='password_form'),
    path('admin/', admin.site.urls),
]
