from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list,name='jobs_home'),
    path('job/<int:id>', views.job_detail, name='job_detail'),
    path('hello/', views.hello, name='hello'),
    path('job/<str:id>', views.job_detail_string),
    path('subscribe/', views.subscribe, name='subscribe'),
]
