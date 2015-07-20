from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)$', views.details, name='details'),
    url(r'^all$', views.shop, name='shop'),
    url(r'^proceed$', views.checkout, name='checkout'),
    url(r'^showcard$', views.showcard, name='showcard'),
    url(r'^login$', views.login, name='login'),
    url(r'^add/$', views.add, name='add'),
    url(r'^add_to_cart/(?P<id>[0-9]+)$', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/$', views.remove, name='remove'),
    url(r'^remove_single/$', views.remove_single, name='remove_single'),
]

