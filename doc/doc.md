django weixin admin文档

---

怎么处理url
---
---
django是一个web开发框架，其中数据库使用类模型，数据库查询语句使用python语言直接实现。

所有的请求都会先进入 \weixin\weixin_mp\urls.py进行url匹配，然后进入url后面的函数进行处理。
例如：*url(r'^weixin/$', 'weixin.views.weixin_main'),*,匹配/weixin/的url都会进入*weixin.views.weixin_main*
进行处理。这个包含三个信息，weixin是app的名字，也就是根目录下类似admin, auto_reply之类的文件夹；
views是这个文件夹中的文件名，views.py文件中，最后是函数名，weixin_main函数。

功能解释
---
---
1 数据库模型
---
见文件\weixin\auto_reply\models.py，每一个回复对应多个关键词，保存回复的类型和每种回复的内容。

其中一个class就是一个数据表，其中的每一项是一个字段。ManyToManyField类似于一条记录的一个字段对应另一个表的多行记录。


2 自定义回复，包括回复文本消息，音乐，多图文；
---
所有的消息都先进入\weixin\weixin\views.py进行处理，区分get和post两种情况（微信验证和接收消息）。微信验证的直接进行判断返回
，而接收消息将xml传递到\weixin\auto_reply\views.py处理。

首先是对消息的类型进行判断，比如是文本消息，图片消息还是点击菜单
事件。现在只能识别文本消息和菜单点击事件，其实处理逻辑是一样的。

不能回复的消息查询数据库，
回复类似“不支持的消息类型”， “我们已经收到消息”等等。最好不要硬编码到代码中，可以在数据库中存储，能随时修改。

每个菜单点击之后接收到的xml文件都有一个key，把这个key加入文本回复的关键词就可以了。

解析xml。这样的话，我们就拿到了一句文本或者一个key（性质一样的）,查询数据库，如果都有对应的关键词，就直接判断这个关键词对应的回复类型和回复内容，

构造xml回复。如果没有找到对应的回复，我是采用了sae自带的中文分词服务，对这句话进行分词，再次判断。
如果还是没有匹配的，就回复消息。
其中有有一种情况比较难处理，就是比如查询天气，是没办法直接查询数据库的，而是类似于执行动作，
可以把关键词出发什么动作，需要什么参数保存在数据库。

比如 天气 这个关键词，我保存的是action get_weather，后面判断回复类型的时候直接执行get_weather()函数。



3 构造回复xml
---
这个主要是在\weixin\auto_reply\reply.py文件中，构造对应的xml。
其中注意音乐回复的xml，不需要ThumbMediaId,去掉那一行就可以。

4 附加服务的实现
---
获取天气预报
*http://developer.baidu.com/map/carapi-7.htm*
我的代码里面有key,可以直接去用。 
 
获取空气质量状况
*http://www.pm25.in/*
这个token比较难申请，我的代码里面的也可以直接去用。

github样式丢失
*185.31.16.184 github.global.ssl.fastly.net* 加host文件

自定义菜单创建删除
这个不用自己去写代码，使用微信自带的调试工具就可以。
http://mp.weixin.qq.com/debug 使用那个就可以。






    

