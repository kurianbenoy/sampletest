from django.conf.urls import url
from .views import NssForms,nss_feed

urlpatterns = [
	url(r'^forms/$',
		view=NssForms,
		name="form_nss"),
	url(r'^$',view=nss_feed,
		name="feed_nss"),
	]


