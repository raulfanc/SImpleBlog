from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog_app.forms import CreatePostForm
from blog_app.models import *


class home(ListView):
    model = Post
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreate(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'post_create.html'
#   fields = ['title', 'body', 'category', 'author']
#     fields = '__all__'   # this will display all fields in the model


class PostUpdate(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = '__all__'


# delete view
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('index')


# ====================Category Views======================
class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'


class CategoryCreate(CreateView):
    model = Category
    template_name = "category_create.html"
    fields = "__all__"


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category_detail.html'


class CategoryUpdate(UpdateView):
    model = Category
    template_name = "category_update.html"
    fields = "__all__"


# delete view
class CategoryDelete(DeleteView):
    model = Category
    template_name = "category_delete.html"
    success_url = reverse_lazy("category_list")
# ====================End======================


# ====================Profile Views======================
class ProfileCreate(CreateView):
    model = Profile
    template_name = "profile_create.html"
    fields = "__all__"


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    fields = '__all__'


class ProfileUpdate(UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    fields = ["address", "phone_number", "web_page"]