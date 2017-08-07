
from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    # /core/

    url(r'^$', views.index, name='index'),

    # /core/712/
    url(r'^(?P<activity_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

]
