from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include("blog.urls")),

]

