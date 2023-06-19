from django.urls import path
from .views import post_list, post_detail, post_create

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/create/', post_create, name='post_create'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]
