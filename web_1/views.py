from datetime import datetime

from django.http import Http404
from django.shortcuts import render

from web_1.models import Article


# Create your views here.
def accueil(request):
    return render(request, 'web_1/accueil.html')

def article(request):
    articles = Article.objects.all()
    return render(request, 'web_1/article.html', {'derniers_articles': articles})

def date_actuelle(request):
    return render(request, 'web_1/date.html', {'date': datetime.now()})


def tweet(request):
    return render(request, 'web_1/tweet_test.html')


def tweet2(request):
    return render(request, 'web_1/tweet_test_2.html')

def lire(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'web_1/lire.html', {'article': article})

