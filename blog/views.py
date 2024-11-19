# Views always need to return an http response or an error
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog\\home.html', context)

# Essa class tem todas as vars necessárias para a home
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']         # Sem isso, ou se simplesmente fosse ['date_posted'], os posts estavam sendo organizados do mais velho ao mais novo. O sinal de menos faz o contrário. Queria que fosse apenas um sorted() pra ficar mais integrado com o python
    paginate_by = 5


# Essa tem todas as necessárias para mostrar post de apenas um usuário
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        return Post.objects.filter(author= user).order_by('-date_posted')


# Essa tem as necessárias para a visualização de um único post
class PostDetailView(DetailView):
    model = Post


# Essa para a criação de um post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


#Essa é para mudar o conteúdo de um post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Essa para deletar um post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog\\about.html', {'title': 'About'})


# blog -> templates -> blog - htmls files