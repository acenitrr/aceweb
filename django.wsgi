import os
import sys

path='/var/www/aceweb'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ace_webserver.settings'
activate_this =path+'/env/bin/activate_this.py'

execfile(activate_this, dict(__file__=activate_this))
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
