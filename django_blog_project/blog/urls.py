from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(),name='blog-home'),
    path('about/', views.about,name='blog-about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(),name='post-detail'),#- trqbva da e pk(primary key) zashtoto PostDetailView tova ochakva
    path('post/new/', views.PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(),name='post-delete'),
    path('post/<str:username>/', views.UserListView.as_view(),name='user-post'),
]