# blog/urls.py
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path(
        'category/<slug:category_slug>/',
        views.category_posts,
        name='category_posts'
    ),
    path('profile/<str:username>/', views.profile, name='profile'),
]
# urlpatterns = [
#     path('posts/<post_id>/edit/', views.post_edit, name='edit'),
#     path('create/', views.post_create, name='create'),
#     path('group/<slug:slug>/', views.group_posts, name='group_list'),
#     path('', views.index, name='index'),
#     path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
#     path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment')