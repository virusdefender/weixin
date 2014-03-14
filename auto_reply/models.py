#coding=utf-8
from django.db import models


#用于图文回复的
class News(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    #图片链接，支持JPG、PNG格式，较好的效果为大图360*200，小图200*200
    pic_url = models.URLField(blank=True)
    #点击图文消息跳转链接
    url = models.URLField(blank=True)

    def __unicode__(self):
        return "%s" % (self.title, )

    class Meta:
        verbose_name_plural = "news"


class Reply(models.Model):
    reply_type_choice = (("text", "Text"), ("news", "Multi pics"), ("music", "Music"), ("action", "Action"), )
    reply_type = models.CharField(max_length=10, choices=reply_type_choice)
    #下面用于纯文本回复
    text_reply = models.TextField(blank=True)
    #下面的用于图文回复
    news_reply = models.ManyToManyField(News, blank=True)
    #下面是回复音乐
    music_title = models.CharField(max_length=40, blank=True)
    music_description = models.CharField(max_length=40, blank=True)
    music_url = models.URLField(blank=True)
    music_hq_url = models.URLField(blank=True)
    #下面是使用action回复的
    action = models.CharField(max_length=30, blank=True)
    parameter = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return "%s" % (self.reply_type, )


class Keyword(models.Model):
    keyword = models.CharField(max_length=20)
    reply = models.ForeignKey(Reply)

    def __unicode__(self):
        return "%s %s" % (self.keyword, self.reply)