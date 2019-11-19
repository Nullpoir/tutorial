from django.db import models
from tinymce import HTMLField
from datetime import datetime
from django.utils import timezone
from django.db.models import Q


#記事本体
class Article(models.Model):

    # 記事データ
    title = models.CharField(verbose_name="タイトル",max_length=100)
    pub_date = models.DateTimeField(verbose_name="公開時間",default=datetime.now)
    body = HTMLField("body")

    # 表示を降べきにするためのコード
    class Meta:
        ordering = ["-pub_date"]
    # 管理画面での表示を変えるコード
    def __str__(self):
        return self.title
