from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator


from News.models import Article


def index(request):
    all_article = Article.objects.all().filter(is_published=True)
    all_article = Paginator(all_article, 5)
    article_on_page = all_article.page(1)
    context = {
        'articles': article_on_page,
    }
    return render(request, 'News/index.html', context)


def news(request, id):
    article = Article.objects.get(pk=int(id))
    context = {
        'article': article,
    }
    return render(request, 'News/news.html', context)


def ajax(request, page):
    if request.is_ajax():
        all_article = Article.objects.all().filter(is_published=True)
        all_article = Paginator(all_article, 5)
        article_on_page = all_article.page(page)
        context = {
            'article': article_on_page,
        }
        return render(request, 'News/ajax.html', context)
    else:
        raise Http404
