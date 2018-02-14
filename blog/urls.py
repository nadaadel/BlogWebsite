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
    url(r'^(?P<pt_id>[0-9]+)/delete$', views.delete),
    url(r'^allcategories_admin/$', views.allcategories_admin),
    url(r'^(?P<ct_id>[0-9]+)/delete_category$', views.delete_category),
    url(r'^allusers_admin/$', views.allusers_admin),
    url(r'^(?P<ut_id>[0-9]+)/delete_user$', views.delete_user),
    url(r'^allwords_admin/$', views.allwords_admin),
    url(r'^(?P<wt_id>[0-9]+)/delete_word$', views.delete_word),



]
# urlpatterns += patterns('',
#                         url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')), )
#
# urlpatterns += staticfiles_urlpatterns()
