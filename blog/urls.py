from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$',views.home),
    url(r'^login$',views.login_form),
    url(r'^register$', views.register_form),
    url(r'^logout$', views.user_logout),
    url(r'^about$', views.get_about),
    url(r'^contact$', views.get_contact),
    url(r'^addcat$', views.addCat),
    url(r'^getcat$', views.getCat),
    url(r'^addpost$', views.addPost),
    url(r'^test$', views.postshow),
    url(r'^single/(?P<post_id>[0-9]+)$', views.get_post),
    url(r'^del/(?P<post_id>[0-9]+)$', views.post_delete),
    url(r'^single/ajax$', views.checkLike),
    url(r'^single/ajaxdis$', views.checkdisLike),
]
# urlpatterns += patterns('',
#                         url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')), )
#
# urlpatterns += staticfiles_urlpatterns()