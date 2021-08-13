from django.contrib import admin
from django.urls import path, include

from homepage.views import IndexView, UserView, BlogView, loginView

app_name='homepage'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('users', UserView.as_view(), name='users'),
    path('login', loginView, name='login'),
    path('blog/<str:blog_pk>', BlogView.as_view(), name='blog'),
]
