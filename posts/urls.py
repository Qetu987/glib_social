from django.urls import path
from posts.views import HomePage, CreatePost

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('post_create/', CreatePost.as_view(), name='post_create'),
] 