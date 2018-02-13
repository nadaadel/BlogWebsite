from django.conf.urls import include, url
from django.contrib import admin
from blog import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$',views.get_home),
    url(r'^login$',views.login_form),
    url(r'^register$', views.register_form),
    url(r'^logout$', views.user_logout),
]

