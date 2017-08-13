from django.db import models
from b_user.models import User


# Create your models here.

class Type(models.Model):
    Type_name = models.CharField(max_length=20)


class Article(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    article_user_like = models.ManyToManyField(User, blank=True)
    article_type = models.ManyToManyField(Type, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    published = models.BooleanField('notDraft', default=True)
    like_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    keep_num = models.IntegerField(default=0)
    article_by_author = models.ForeignKey(User,max_length=40,related_name='article_author')


class Comment(models.Model):
    comment_user = models.ForeignKey(User)
    comment_article = models.ForeignKey(Article)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    like_num = models.IntegerField(default=0)

    def __str__(self):
        return self.content


class Like(models.Model):
    Like_by_user = models.ForeignKey(User, null=True)
    Like_article = models.ForeignKey(Article, null=True)
    comment = models.ForeignKey(Comment, null=True)
