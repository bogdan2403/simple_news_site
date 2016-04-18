from django.http import Http404
from django.shortcuts import render

from News import num
from News.models import Article


def index(request):
    num.page = 1
    article_on_page = num.pages(Article.objects.all().filter(is_published=True))
    context = {
        'articles': article_on_page,
    }
    return render(request, 'news/index.html', context)


def news(request, id):
    article = Article.objects.get(pk=int(id))
    context = {
        'article': article,
    }
    return render(request, 'news/news.html', context)


def ajax(request):
    if request.is_ajax():
        num.page += 1
        article_on_page = num.pages(Article.objects.all().filter(is_published=True))
        context = {
            'article': article_on_page,
        }
        return render(request, 'news/ajax.html', context)
    else:
        raise Http404
