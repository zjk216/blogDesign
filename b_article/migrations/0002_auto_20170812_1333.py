# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('b_article', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='Like_by_user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(null=True, to='b_article.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_article',
            field=models.ForeignKey(to='b_article.Article'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='article_by_author',
            field=models.ForeignKey(max_length=40, related_name='article_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.ManyToManyField(to='b_article.Type'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_user_like',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
