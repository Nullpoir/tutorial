from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.TopPageView,name="Top"),
    path('article/<int:pk>',views.ArticleView,name="Article"),#追加
]
