#coding=utf-8

from django.contrib import admin
from auto_reply.models import Keyword, Reply, News


class KeywordInline(admin.StackedInline):
    model = Keyword
    extra = 2


class ReplyAdmin(admin.ModelAdmin):
    inlines = [KeywordInline, ]
    list_display = ("text_reply", "reply_type", )
    fieldsets = [
        (None, {"fields": ["reply_type"]}),
        ("Text Reply", {"fields": ["text_reply", ]}),
        ("Multi Pics Reply", {"fields": ["news_reply", ]}),
        ("Music Reply", {"fields": ["music_title", "music_description", "music_url", "music_hq_url", ]}),
        ("Action", {"fields": ["action", "parameter", ]}),
    ]


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", )


admin.site.register(Reply, ReplyAdmin)
admin.site.register(News, NewsAdmin)
