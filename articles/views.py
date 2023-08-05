from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article
from hitcount.views import HitCountDetailView
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(LoginRequiredMixin, HitCountDetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'
    count_hit = True


class ArticleUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'body', 'photo')
    template_name = 'article_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    success_url = reverse_lazy('article_list')
    fields = ('title', 'body', 'photo')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
