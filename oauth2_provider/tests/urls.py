from django.urls import include, re_path
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^o/', include(('oauth2_provider.urls', 'oauth2_provider'), namespace='oauth2_provider')),
]
