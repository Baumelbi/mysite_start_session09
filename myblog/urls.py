from django.conf.urls import url
from myblog.views import stub_view
from myblog.views import list_view
from myblog.views import detail_view
from django.conf.urls import url
from myblog.latestentriesfeed import LatestEntriesFeed

urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),

    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name="blog_detail"),

    url(r'^feed/$', LatestEntriesFeed()),

]
