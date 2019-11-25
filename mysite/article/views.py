from django.shortcuts import render
from .models import Article #追加
# Create your views here.

def TopPageView(requests):
    return render(requests,"index.html")

def ArticleView(request,pk):
    article = Article.objects.get(pk=pk)
    context = {"article":article}
    return render(request,"article/article.html",context)
