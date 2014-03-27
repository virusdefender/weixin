#coding=utf-8
import json
import urllib2


#获取空气质量状况
def get_air_quality():
    req = urllib2.Request("http://www.pm25.in/api/querys/pm2_5.json?city=qingdao&token=5TpZRDLoXrsxAnZWUhnR&stations=no")
    response = urllib2.urlopen(req).read()
    response = json.loads(response)[0]
    return u"实时空气质量：" + response["quality"] + u"，pm2.5：" + str(response["pm2_5"])


#获取天气http://developer.baidu.com/map/carapi-7.htm
def get_weather(city="青岛"):
    url = u"http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=bldsc4KQ5dvqj1T1YDxIDCmz" % city
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    content = json.loads(response.read())
    weather_list = content["results"][0]["weather_data"]
    day1 = weather_list[0]["date"] + u"，" + weather_list[0]["weather"] + u"，" + weather_list[0]["wind"] + u"，" + \
        weather_list[0]["temperature"]
    day2 = weather_list[1]["date"] + u"，" + weather_list[1]["weather"] + u"，" + weather_list[0]["wind"] + u"，" + \
        weather_list[1]["temperature"]
    day3 = weather_list[2]["date"] + u"，" + weather_list[2]["weather"] + u"，" + weather_list[0]["wind"] + u"，" + \
        weather_list[2]["temperature"]
    return u"青岛：" + day1 + "\n" + day2 + "\n" + day3 + "\n" + get_air_quality()