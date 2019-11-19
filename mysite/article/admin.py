from django.contrib import admin
from .models import Article #追加
# 以下に追加
admin.site.register(Article)
