#coding=utf-8
import urllib
import urllib2
import json
from django.http import HttpResponse
from lxml import etree
from auto_reply.models import Keyword, Reply
from auto_reply.reply import auto_reply


def chinese_segment(content):
    _SEGMENT_BASE_URL = 'http://segment.sae.sina.com.cn/urlclient.php'
    payload = urllib.urlencode([('context', content.encode("utf-8")), ])
    args = urllib.urlencode([('word_tag', 1), ('encoding', 'UTF-8'), ])
    url = _SEGMENT_BASE_URL + '?' + args
    result = urllib2.urlopen(url, payload).read()
    return json.loads(result)


def find_keyword(content):
    reply = Keyword.objects.filter(keyword=content)
    if len(reply):
        return True
    else:
        return False


def find_reply(from_username, content):
    """查找文本消息是否有对应的回复  如果没有的话 进行中文分词 并再次判断
    """
    reply = find_keyword(content)
    if reply is False:
        #直接查找没有找到对应的回复，这个时候对content进行中文分词
        segment_result = chinese_segment(content)
        segment_length = len(segment_result)
        while segment_length:
            segment_length -= 1
            content = segment_result[segment_length]["word"]
            reply = find_keyword(content)
            if reply is False:
                continue
            else:
                return auto_reply(from_username, content)
        return auto_reply(from_username, u"没有找到合适的回复")
    else:
        return auto_reply(from_username, content)


def auto_reply_main(request_xml):
    """识别消息的类型 分类处理
    """
    msg_type = request_xml.find("MsgType").text
    from_user_name = request_xml.find("FromUserName").text
    if msg_type == "text":
        content = request_xml.find("Content").text
        return HttpResponse(find_reply(from_user_name, content))
    elif msg_type == "event":
        event = request_xml.find("Event").text
        if event == "subscribe":
            return HttpResponse(find_reply(from_user_name, "用户关注事件"))
        elif event == "unsubscribe":
            return HttpResponse("Got it")
        elif event == "CLICK":
            event_key = request_xml.find("EventKey").text
            return HttpResponse(find_reply(from_user_name, event_key))
    else:
        return HttpResponse(find_reply(from_user_name, "不支持的消息类型"))
