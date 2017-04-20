#coding:utf-8
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'love.settings'

from django.core.wsgi import get_wsgi_application
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(get_wsgi_application())
