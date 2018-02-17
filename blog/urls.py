from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^home$',views.home),
    url(r'^login$',views.login_form),
    url(r'^register$', views.register_form),
    url(r'^logout$', views.user_logout),
    url(r'^about$', views.get_about),
    url(r'^contact$', views.get_contact),
    url(r'^adminModify$', views.admin),
    url(r'^allposts_admin/$', views.allPosts_admin),
    url(r'^(?P<pt_id>[0-9]+)/delete$', views.delete),
    url(r'^addPost_admin$', views.addPost_admin),
    url(r'^(?P<pt_id>[0-9]+)/update_post', views.update_post),
    url(r'^(?P<pt_id>[0-9]+)$',  views.getPost),
    url(r'^allcategories_admin/$', views.allcategories_admin),
    url(r'^(?P<ct_id>[0-9]+)/delete_category$', views.delete_category),
    url (r'^new/$', views.addCategory),
    url(r'^(?P<ct_id>[0-9]+)/update_category$', views.update_category),
    url(r'^allusers_admin/$', views.allusers_admin),
    url(r'^(?P<ut_id>[0-9]+)/delete_user$', views.delete_user),
    url(r'^(?P<ut_id>[0-9]+)/block$', views.block),
    url(r'^(?P<ut_id>[0-9]+)/unblock$', views.unblock),
    url(r'^(?P<ut_id>[0-9]+)/promote$', views.promote),
    url(r'^(?P<ut_id>[0-9]+)/unpromote$', views.unpromote),
    url(r'^allwords_admin$', views.allwords_admin),
    url(r'^(?P<wt_id>[0-9]+)/delete_word$', views.delete_word),
    url (r'^newWord$', views.addWords),
    url(r'^(?P<wt_id>[0-9]+)/update_word$', views.update_word),
    # url(r'^single$', views.get_post),
    url(r'^test/(?P<cat_id>[0-9]+)$', views.allsub),
    url(r'^single/(?P<post_id>[0-9]+)$', views.getPost),
    url(r'^getcat$', views.getCat),
    url(r'^sub/(?P<cat_id>[0-9]+)$', views.sub),
    url(r'^unsub/(?P<cat_id>[0-9]+)$', views.unsub),
    url (r'^newtag', views.addTag),

]
# urlpatterns += patterns('',
#                         url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')), )
#
# urlpatterns += staticfiles_urlpatterns()