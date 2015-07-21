from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)$', views.details, name='details'),
    url(r'^all$', views.shop, name='shop'),
    url(r'^proceed$', views.checkout, name='checkout'),
    url(r'^showcart$', views.showcart, name='showcart'),
    url(r'^login$', views.login, name='login'),
    url(r'^add/(?P<id>[0-9]+)/$', views.add, name='add'),
    url(r'^add_to_cart/(?P<id>[0-9]+)/$', views.add_to_cart, name='add_to_cart'),  # !!!! careful with "/$" !!!!!
    url(r'^remove/(?P<id>[0-9]+)/$', views.remove, name='remove'),
    url(r'^remove_single/(?P<id>[0-9]+)/$', views.remove_single, name='remove_single'),
    ##url(r'^products/$', views.shop, name='shop'),                                # for testing purposes only
]
