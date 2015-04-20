from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/events/(?P<pyear>\d{4})/(?P<pmonth>\d{2})/$', views.events, name='events'),
    url(r'^/events/$', views.events, name='events'),
    url(r'^/yearlyevents/(?P<pmonth>\d{2})/$', views.yearlyevents, name='yearlyevents'),
    url(r'^/yearlyevents/$', views.yearlyevents, name='yearlyevents'),
    url(r'^/date/(?P<pmonth>\d{2})/(?P<pday>\d{2})/$', views.datedisp, name='events'),
    url(r'^/darshan/$', views.darshan, name='darshan'),
    url(r'^/photos/$', views.photos, name='photos'),
    url(r'^/demo_light_skin/$', views.demo_light_skin, name='demo_light_skin'),
    url(r'^/volunteer/$', views.volunteer, name='volunteer'),
    url(r'^/hall/$', views.hall, name='hall'),
    url(r'^/contact/$', views.contact, name='contact'),
    url(r'^/about/$', views.about, name='about'),
]
