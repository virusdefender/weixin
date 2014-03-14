#coding=utf-8
import json
import urllib
import urllib2
import time
import random
from auto_reply.models import Keyword, Reply
from auto_reply.classroom import get_classroom_api
from auto_reply.weather import get_weather
from weixin_mp.config import WEIXIN_ID


def text_reply_xml(to_username, text):
    """构造文本回复的xml
    """
    xml = u"""
            <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>""" % (to_username, WEIXIN_ID, str(int(time.time())), text)
    return xml


def music_reply_xml(to_username, title, description, music_url, hq_music_url):
    """构造音乐回复的xml
    """
    xml = u"""
            <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[music]]></MsgType>
            <Music>
            <Title><![CDATA[%s]]></Title>
            <Description><![CDATA[%s]]></Description>
            <MusicUrl><![CDATA[%s]]></MusicUrl>
            <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>
            </Music>
            </xml>
            """ % (to_username, WEIXIN_ID, str(int(time.time())), title, description, music_url, hq_music_url)
    return xml


def news_reply_xml(to_username, news):
    news_num = len(news)
    xml = u"""
            <xml>
            <ToUserName><![CDATA[{0}]]></ToUserName>
            <FromUserName><![CDATA[{1}]]></FromUserName>
            <CreateTime>[{2}</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>{3}]</ArticleCount>
            <Articles>
        """.format(to_username, WEIXIN_ID, str(int(time.time())), news_num)
    num = news_num
    for num in range(0, news_num):
        item_xml = u"""
                   <item>
                   <Title><![CDATA[{0}]]></Title>
                   <Description><![CDATA[{1}]]></Description>
                   <PicUrl><![CDATA[{2}]]]></PicUrl>
                   <Url><![CDATA[{3}]]></Url>
                   </item>
               """.format(news[num].title, news[num].description, news[num].pic_url, news[num].url)
        xml += item_xml

    xml += u"""
             </Articles>
             </xml>
           """
    return xml


def auto_reply(from_username, content):
    """根据content选择合适的回复 构造xml 返回
    """
    reply = Keyword.objects.filter(keyword=content)
    print str(reply[0].reply)
    if len(reply) > 1:
        reply = reply[random.randint(0, len(reply) - 1)]
    else:
        reply = reply[0]

    if reply.reply.reply_type == "action":
        #test
        if reply.reply.action == "classroom":
            return text_reply_xml(from_username, get_classroom_api(reply.reply.parameter))
        elif reply.reply.action == "weather":
            return text_reply_xml(from_username, get_weather())
    elif reply.reply.reply_type == "text":
        return text_reply_xml(from_username, reply.reply.text_reply)
    elif reply.reply.reply_type == "news":
        return news_reply_xml(from_username, reply.reply.news_reply.all())
    elif reply.reply.reply_type == "music":
        return music_reply_xml(from_username, reply.reply.music_title, reply.reply.music_description,
                               reply.reply.music_url, reply.reply.music_hq_url)
    else:
        print u"错误的回复类型"



