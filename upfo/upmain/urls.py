from django.conf.urls.defaults import *

urlpatterns = patterns('upfo.upmain.views',
    url(r'^/?$', "test_index", name="index"),
    url(r'^after/?$', "after", name="after"),
)
