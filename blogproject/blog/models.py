from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# 分类
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 文章
class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文
    body = models.TextField()

    # 创建时间
    create_time = models.DateTimeField()
    # 修改时间
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)

    # 一个分类下有多篇文章
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 一篇文章有多个标签,一个标签下也可能有多篇文章
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
