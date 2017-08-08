from django.conf.urls import url
from .views import NssForms

urlpatterns = [
	url(r'^forms/$',
		view=NssForms,
		name="form_nss"),
	]


