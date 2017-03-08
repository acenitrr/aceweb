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
from login.views import import_login_table,email_verification,signup_view,login_view
from student.views import student_profile,student_group_profile,edit_student_profile,signup_student
from faculty.views import faculty_profile,faculty_group_profile,edit_faculty_profile,signup_faculty
from alumni.views import alumni_profile,alumni_group_profile,edit_alumni_profile,signup_alumni
from forgot_password.views import forgot_password_view,verify_forgot_password
from announcement.views import announcement
from project.views import project
from notice.views import get_notice,notice_read,home,administration,logout_view,activities
from django.views.generic.base import RedirectView
from achievement.views import achievements

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^import/',import_login_table),
    url(r'^verify_email/(?P<value>.+)/$',email_verification),
    url(r'^signup/',signup_view),
    url(r'^student_view/(?P<roll_no>.+)/$',student_profile),
    url(r'^faculty_view/(?P<faculty_id>.+)/$',faculty_profile),
    url(r'^alumni_view/(?P<roll_no>.+)/$',alumni_profile),
    url(r'^students_profile/$',student_group_profile),
    url(r'^faculty_profile/$',faculty_group_profile),
    url(r'^alumni_profile/$',alumni_group_profile),
    url(r'^forgot_password/$',forgot_password_view),
    url(r'^verify_forgot_password/(?P<value>.+)/$',verify_forgot_password),
    url(r'^edit_student_profile/$',edit_student_profile),
    url(r'^edit_faculty_profile/$',edit_faculty_profile),
    url(r'^edit_alumni_profile/$',edit_alumni_profile),
    url(r'^signup_student/$',signup_student),
    url(r'^signup_faculty/$',signup_faculty),
    url(r'^signup_alumni/$',signup_alumni),
    url(r'^login/$',login_view),
    url(r'^announcement/$',announcement),
    url(r'^notice_get$',get_notice),
    url(r'^notice_read$',notice_read),
    url(r'^$',home),
    url(r'^home/$',home),
    url(r'^academics/$',project),
    url(r'^activities/$',activities),
        url(r'^achievements/$',achievements),
    url(r'^administration/$',administration),
    url(r'^logout/$',logout_view),

    # url(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='index')

    #url(r'^profile/(?P<value>.+)/(?P<value>.+)',signup_view),
    #url(r'^profile_search/',signup_view),
    #url(r'^notice/$',signup_view),
    #url(r'^announcement/',signup_view),
    #url(r'^syllabus/$',signup_view),
    #url(r'^academics/',signup_view),

]
admin.site.site_header = "CSE Administration"
admin.site.index_title = 'ACE Website'
admin.site.site_title = 'CSE'

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
