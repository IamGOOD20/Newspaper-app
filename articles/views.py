from django.views.generic import TemplateView


class ArticlesList(TemplateView):
    template_name = 'articles/articleslist.html'
