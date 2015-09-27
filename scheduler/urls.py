# coding: utf-8

from django.conf.urls import url

from .views import HomeView, HomeViewHU, HelpDesk, PlannerView

urlpatterns = [
    url(r'^$', HomeView.as_view(template_name="home_i18l.html")),
    url(r'^hu/$', HomeViewHU.as_view(template_name="home_HU.html")),
    url(r'^helpdesk/$', HelpDesk.as_view(), name="helpdesk"),
    url(
        r'^helpdesk/location/(?P<pk>\d+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        PlannerView.as_view(),
        name="planner_by_location"),
]
