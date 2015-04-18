from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/events/(?P<pyear>\d{4})/(?P<pmonth>\d{2})/$', views.events, name='events'),
    url(r'^/events/$', views.events, name='events'),
    url(r'^/yearlyevents/(?P<pmonth>\d{2})/$', views.yearlyevents, name='yearlyevents'),
    url(r'^/yearlyevents/$', views.yearlyevents, name='yearlyevents'),
    url(r'^/date/(?P<pmonth>\d{2})/(?P<pday>\d{2})/$', views.datedisp, name='events'),
]
