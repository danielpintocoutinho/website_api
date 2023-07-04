from django.urls import path

from posts import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<str:pk>', views.PostDetail.as_view(), name='post-detail')
]