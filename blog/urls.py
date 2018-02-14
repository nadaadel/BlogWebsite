from django.conf.urls import include, url
#from django.contrib import admin
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^home$',views.home),
    url(r'^login$',views.login_form),
    url(r'^register$', views.register_form),
    url(r'^logout$', views.user_logout),
    url(r'^about$', views.get_about),
    url(r'^contact$', views.get_contact),
    url(r'^adminModify$', views.admin),
    url(r'^allposts_admin/$', views.allPosts_admin),
    url(r'^(?P<pt_id>[0-9]+)/delete', views.delete),



]
# urlpatterns += patterns('',
#                         url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')), )
#
# urlpatterns += staticfiles_urlpatterns()
