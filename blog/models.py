from django.db import models


# Create your models here.
class Article(models.Model):
    # id
    article_id = models.AutoField(primary_key=True)
    # 文章的标题
    title = models.TextField()
    # 文章的摘要
    brief = models.TextField()
    # 文章的内容
    content = models.TextField()
    # 文章的日期
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    pass
