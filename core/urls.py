
from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    # /core/

    url(r'^$', views.homepage, name='homepage'),

    url(r'^index/$', views.index, name='index'),

    url(r'^aboutus/$', views.aboutus, name='aboutus'),

    # /core/7/
    url(r'^(?P<activity_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    #core/7/favorite
    url(r'^(?P<activity_id>[0-9]+)/add_total/$', views.add_total, name='add_total'),
]
