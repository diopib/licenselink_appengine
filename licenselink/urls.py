from django.conf.urls import patterns, include, url
from views import HomeView, CreateSuccess, ViewLicense

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', HomeView.as_view()),
    url(r'^(?P<short_url>\w{6})/$', ViewLicense.as_view(), name='view_license'),
    url(r'^success/(?P<short_url>\w{6})/$', CreateSuccess.as_view(), name='create_success'),
    url(r'^admin/', include(admin.site.urls)),
)
