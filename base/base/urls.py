from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'', include('app.urls', namespace='app')),
	url(r'^users/', include('users.urls', namespace='users')),
]