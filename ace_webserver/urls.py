"""ace_webserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from login.views import import_login_table,email_verification,signup_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^import/',import_login_table),
    url(r'^verify_email/(?P<value>.+)/$',email_verification),
    url(r'^signup/',signup_view),
    #url(r'^profile/(?P<value>.+)/(?P<value>.+)',signup_view),
    #url(r'^profile_search/',signup_view),
    #url(r'^notice/$',signup_view),
    #url(r'^announcement/',signup_view),
    #url(r'^syllabus/$',signup_view),
    #url(r'^academics/',signup_view),

]
admin.site.site_header = "CSE Administration"#"Code Nicely's Administration"
admin.site.index_title = 'ACE Website'
admin.site.site_title = 'CSE'

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
