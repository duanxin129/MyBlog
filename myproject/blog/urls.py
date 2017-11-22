from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    #文章详情url
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name = 'detail'),
    #归档
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
]