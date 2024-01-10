from django.contrib.auth.mixins import (
    UserPassesTestMixin,
    LoginRequiredMixin,
)
from django.views.generic import (
    ListView,
    DetailView)

from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Artiicle
from django.urls import reverse_lazy
class ArticleListView(LoginRequiredMixin, ListView):
    model = Artiicle
    template_name = 'article_list.html'

class ArticleUpdateView(
    UserPassesTestMixin,
    LoginRequiredMixin,
    UpdateView
):
    model = Artiicle
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(
    UserPassesTestMixin,
    LoginRequiredMixin,
    DeleteView
):
    model = Artiicle
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Artiicle
    template_name = 'article_detail.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Artiicle
    fields = ('title', 'body',)
    template_name = 'article_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


