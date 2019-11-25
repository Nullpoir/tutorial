from django.shortcuts import render
from .models import Article #追加
# Create your views here.

def TopPageView(requests):
    #追加
    articles = Article.objects.all()
    context = {"articles":articles}
    #ここまで
    return render(requests,"index.html",context)

def ArticleView(request,pk):
    article = Article.objects.get(pk=pk)
    context = {"article":article}
    return render(request,"article/article.html",context)
