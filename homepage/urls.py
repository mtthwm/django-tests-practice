from django.contrib import admin
from django.urls import path, include

from homepage.views import UserView, BlogView, loginView, AboutView, ResumeView, BlogListView

app_name='homepage'
urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('users', UserView.as_view(), name='users'),
    path('login', loginView, name='login'),
    path('blog', BlogListView.as_view(), name="blogs"),
    path('blog/<str:blog_pk>', BlogView.as_view(), name='blog'),
    path('resume', ResumeView.as_view(), name='resume')
]
