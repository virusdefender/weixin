#coding=utf-8
import hashlib
import json
from lxml import etree
from weixin_mp.config import WEIXIN_TOKEN
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from auto_reply.views import auto_reply_main


@csrf_exempt
def weixin_main(request):
    """所有的消息都会先进入这个函数进行处理，函数包含两个功能，如果请求时get，说明是微信接入验证，如果是post就是微信正常的收发消息。
    """
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("weixin  index")
    else:
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        response_xml = auto_reply_main(request_xml)
        return HttpResponse(response_xml)