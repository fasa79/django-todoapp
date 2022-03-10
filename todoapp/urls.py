"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('', views.showCategoryTask, name='home'),

    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/user/', views.showUserProfile, name='showUserProfile'),
    path('accounts/user/update', views.editUserProfile, name='editUserProfile'),
    path('accounts/user/change-password', views.changePassword, name='changePassword'),
    path('register/', views.register, name='register'),

    path('category/add/', views.addCategory, name='addCategory'),
    path('category/<id>/delete/', views.delCategory, name='delCategory'),
    path('task/add/', views.addTask, name='addTask'),
    path('task/<id>/delete/', views.delTask, name='delTask'),
]
