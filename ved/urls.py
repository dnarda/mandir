from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^t2/$', views.t2, name='test'),
    url(r'^events/(?P<pyear>\d{4})/(?P<pmonth>\d{2})/$', views.events, name='events'),
    url(r'^date/(?P<pmonth>\d{2})/(?P<pday>\d{2})/$', views.datedisp, name='events'),
]
