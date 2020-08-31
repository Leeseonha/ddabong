"""ddabong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import contact.views
import ddabong.items.views
import ddabong.mypage.views
import ddabong.theme.views
import ddabong.voulunteer_work.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ddabong.theme.urls')),
    path('v_area/',  ddabong.voulunteer_work.views.v_area, name='v_area'),
    path('v_all/',  ddabong.voulunteer_work.views.v_all, name='v_all'),
    path('v_detail/',  ddabong.voulunteer_work.views.v_detail, name='v_detail'),
    path('mypage/',  ddabong.mypage.views.mypage, name='mypage'),
    path('items/', ddabong.items.views.items, name='items'),
]
