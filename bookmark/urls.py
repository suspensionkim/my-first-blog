from django.conf.urls import url
from bookmark.views import BookmarkLV, BookmarkDV
# from bookmark.views import bookmark_list, bookmark_detail  # 추가

app_name='bookmark'

urlpatterns = [
     url(r'^$', BookmarkLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]