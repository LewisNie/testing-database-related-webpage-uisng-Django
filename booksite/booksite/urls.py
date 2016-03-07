from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'booksite.views.home', name='home'),
    url(r'^catalog/', include('catalog.urls', namespace='catalog')),
    url(r'^admin/', include(admin.site.urls)),
]
