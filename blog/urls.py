from django.urls import path
from .views import PostListView, UserPostListView , PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name= 'blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name= 'user-posts'),
    path('post/new/', PostCreateView.as_view(), name= 'post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name= 'post-detail'),      # pk de primary key (pode ser mudado colocando um atributo na class, mas esse é o default para o DetailView). O int é pra limitar essa key para penas números. É uma forma de criar páginas on the go
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name= 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name= 'post-delete'),
    path('about/', views.about, name= 'blog-about'),
]
