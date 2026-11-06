from __future__ import absolute_import
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^authorize/$', views.AuthorizationView.as_view(), name="authorize"),
    re_path(r'^token/$', views.TokenView.as_view(), name="token"),
    re_path(r'^revoke_token/$', views.RevokeTokenView.as_view(), name="revoke-token"),
]

# Application management views
urlpatterns += [
    re_path(r'^applications/$', views.ApplicationList.as_view(), name="list"),
    re_path(r'^applications/register/$', views.ApplicationRegistration.as_view(), name="register"),
    re_path(r'^applications/(?P<pk>\d+)/$', views.ApplicationDetail.as_view(), name="detail"),
    re_path(r'^applications/(?P<pk>\d+)/delete/$', views.ApplicationDelete.as_view(), name="delete"),
    re_path(r'^applications/(?P<pk>\d+)/update/$', views.ApplicationUpdate.as_view(), name="update"),
]
