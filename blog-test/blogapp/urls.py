from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.post_page, name='post_page'),
    path("accounts/login/", views.loginUser, name="login"),
    path("search/", views.search_blogs, name="search"),
    path("tag/<slug:slug>", views.tag_page, name="tag_page"),
]