from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.allPosts),
    url(r'^add/$',views.addPost),
    url(r'^search/$',views.search),
    url(r'^home/e', views.postshow),
    url(r'^blog/(?P<s_v>\d+)/$', views.postshow, name='sv'),
]