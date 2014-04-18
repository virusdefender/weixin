weixin
======
这是一个简单的使用django写的微信第三方平台。现在是在青岛大学团委 qddxtw 微信公众平台上使用, 可以关注一下，看看效果。

如果需要功能更加强大的，可以参看这个 https://github.com/wwj718/django_weixin_portal

这个平台我一直是在sae上使用的，如果需要在别的地方安装，请自行修改。主要是settings.py中数据库选择部分。

第一次使用请修改  https://github.com/virusdefender/weixin/blob/master/weixin_mp/config.py  里面的值。

----
这个微信公众平台是单用户版的，没有注册登录功能，也只能同时供一个账号使用。
----
这个应用在sae上的部署方法

先在本地python manage.py syncdb之后，使用mysqldump命令导出sql文件，然后是用svn上传，

初始化数据库。然后上传sql文件建立数据路，记住，sql文件中要把所有的lock和unlock语句删掉。

微信验证的url是 /weixin/， 后台是/admin/
