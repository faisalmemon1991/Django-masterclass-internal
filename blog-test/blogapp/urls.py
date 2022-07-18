from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.post_page, name='post_page'),
    path("accounts/login/", views.loginUser, name="login"),
    path("search/", views.search_posts, name="search"),
    path("all_posts/", views.all_posts, name="all_posts"),
    path("all_liked_posts/", views.all_liked_posts, name="all_liked_posts"),
    path("like_post/<slug:slug>", views.like_post, name="like_post"),
    path("about/", views.about, name="about"),
    path("tag/<slug:slug>", views.tag_page, name="tag_page"),

    path("all_bookmarked_posts/", views.all_bookmarked_posts, name="all_bookmarked_posts"),
    path("bookmark_post/<slug:slug>", views.bookmark_post, name="bookmark_post"),
    path("accounts/register/", views.register_user, name="register"),
]