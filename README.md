weixin
======
这是一个简单的使用django写的微信第三方平台。

这个平台我一直是在sae上使用的，如果需要在别的地方安装，请自行修改。

第一次使用请修改  https://github.com/virusdefender/weixin/blob/master/weixin_mp/config.py  里面的值。

----

关于这个应用在sae上的部署，大致就是先在本地python manage.py syncdb之后，使用mysqldump命令导出sql文件，然后在sae里面

上传创建数据库。然后上传代码到服务器。

微信验证的url是 /weixin/
