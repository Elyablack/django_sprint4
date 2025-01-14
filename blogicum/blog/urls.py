from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'category/<slug:category_slug>/',
        views.category_posts,
        name='category_posts'
    ),
    path(
        'posts/<int:post_id>/',
        views.post_detail,
        name='post_detail'
    ),
    path(
        'posts/<int:post_id>/edit/',
        views.post_edit,
        name='post_edit'
    ),
    path(
        'posts/<int:post_id>/delete/',
        views.post_delete,
        name='post_delete'
    ),
    path(
        'profile/<str:username>/',
        views.profile,
        name='profile'
    ),
    path(
        'posts/<int:post_id>/add_comment/',
        views.add_comment,
        name='add_comment'
    ),
    path(
        'posts/<int:post_id>/delete_comment/<int:comment_id>/',
        views.comment_delete,
        name='comment_delete'
    ),
    path(
        'posts/create/',
        views.post_create,
        name='post_create'
    ),
    path(
        'posts/<int:post_id>/edit_comment/<int:comment_id>/',
        views.edit_comment,
        name='edit_comment'
    )
]
