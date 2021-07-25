from django.contrib import admin
from django.urls import path, include

from homepage.views import IndexView, UserView, loginView

urlpatterns = [
    path('', IndexView.as_view()),
    path('users', UserView.as_view()),
    path('login', loginView)
]
