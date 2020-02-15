"""Demo URL Configuration

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
from django.contrib import admin
from django.urls import path,re_path,include
from .views import *
# from app_01 import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/',index),
    # path('about/',about),
    # re_path('about/(\d)/',about),
    # path('indexhtml/',indexhtml),
    # re_path('getindex/(\d)/',getindex),
    # path('get_index/',get_index),
    # path('getIndex/',getIndex),
    # path('template/',template),
    # path('statica/',statica),
    path('about/',about),
    path('index/',index),
    path('listpic/',listpic),
    path('newslistpic/',newslistpic),
    # path('app_01_index',app_views.index)
    # path('Article/',include('Article.urls'))


]
