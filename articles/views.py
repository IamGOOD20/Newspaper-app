from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Artiicle
from django.urls import reverse_lazy
class ArticleListView(ListView):
    model = Artiicle
    template_name = 'article_list.html'

class ArticleUpdateView(UpdateView):
    model = Artiicle
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    # success_url = reverse_lazy('article_list')
class ArticleDeleteView(DeleteView):
    model = Artiicle
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleDetailView(DetailView):
    model = Artiicle
    template_name = 'article_detail.html'

class ArticleCreateView(CreateView):
    model = Artiicle
    fields = ('title', 'body', 'author',)
    template_name = 'article_new.html'
    success_url = reverse_lazy('article_list')
