from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog_app.models import Post, Category


class home(ListView):
    model = Post
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreate(CreateView):
    model = Post
    template_name = 'post_create.html'
#   fields = ['title', 'body', 'category', 'author']
    fields = '__all__'   # this will display all fields in the model


class PostUpdate(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = '__all__'


# delete view
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('index')