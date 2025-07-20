# blog/urls.py
from django.urls import path
from . import views
from django.urls import include

app_name = 'blog'

urlpatterns = [
    path('', views.home_page, name='post-list'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', views.CreatePost.as_view(), name='post-create'),
]
