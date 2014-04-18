#coding=utf-8
############################
#说明：
#这个文件中的查询空教室的功能是我们自己特有的功能，所以使用本开源项目的朋友不用关注这里
############################
import urllib2
import json
import datetime


def get_class():
    hour_now = datetime.datetime.now().hour
    min_now = datetime.datetime.now().minute
    total_min = (hour_now - 8) * 60 + min_now
    if total_min <= 50:
        return 1
    elif 50 < total_min <= 110:
        return 2
    elif 110 < total_min <= 180:
        return 3
    elif 180 < total_min <= 240:
        return 4
    elif 240 < total_min <+ 380:
        return 5
    elif 380 < total_min <= 440:
        return 6
    elif 440 < total_min <= 500:
        return 7
    elif 500 < total_min <= 550:
        return 8
    elif 550 < total_min <= 680:
        return 9
    elif 680 < total_min <= 750:
        return 10
    else:
        return 11

#这个是通过api获取
def get_classroom_api(classroom_name):
    classroom_name_dic = {"boyuan": u"博远楼", "bozhi": u"博知楼", "boxue": u"博学楼", "dong12": u"东12"}
    url = "http://qduyzzdh2.duapp.com/classroom.php?building_name={classroom_name}&token=qddxtwwx".\
        format(classroom_name=classroom_name)
    try:
        response = urllib2.urlopen(url).read()
    except urllib2.URLError:
        return u"查询错误，请稍后重试！"

    response_json = json.loads(response)
    #获取到的json应该是一个列表 然后每一个分列表都是一节课的时候的教室信息
    if str(response_json["error"]) == "0":
        class_num = get_class()
        response_str = u"根据当前时间   青小微为你找到下面这些自习室呦\n"
        if class_num + 4 > 11:
            end_class = 11
        else:
            end_class = class_num + 4
        for class_order in range(class_num, end_class + 1):
            result = ""
            for room in response_json["result"][class_order - 1]:
                result += (room + " ")
            response_str = response_str + (u"第{class_order}节：{result}\n".format(class_order=class_order, result=result))
    elif str(response_json["error"]) == "3":
        return u"周末啦，到处都是空教室，我就不给你查了~~快找个教室学习去吧~"
    else:
        response_str = u"查询错误，请稍后重试！"
    return response_str























