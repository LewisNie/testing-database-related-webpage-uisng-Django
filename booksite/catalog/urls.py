from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /catalog/
    url(r'^$', views.index, name='index'),
    # ex: /catalog/add/publisher/
    url(r'^add/publisher/$', views.add_publisher, name='add_publisher'),
    # ex: /catalog/add/title/
    url(r'^add/title/$', views.add_title, name='add_title'),
    # ex: /catalog/get/titles/by/publisher/
    url(r'^get/titles/by/publisher/$', views.get_titles_by_publisher, name='get_titles_by_publisher'),
    # ex:/catalog/get/publisher/of/title/
    url(r'^get/publisher/of/title/$', views.get_publisher_of_title, name='get_publisher_of_title'),
]
