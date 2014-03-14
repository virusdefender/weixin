import sae
from weixin_mp import wsgi

application = sae.create_wsgi_app(wsgi.application)

