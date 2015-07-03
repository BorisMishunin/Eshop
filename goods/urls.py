from django.conf.urls import include, url, patterns




urlpatterns = [
    # Examples:
    # url(r'^$', 'webcams.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^good_card/get/(?P<Wares_id>\d+)/$', 'goods.views.good_card'),
    url(r'^$', 'goods.views.index'),


]
