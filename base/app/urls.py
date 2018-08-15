from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
	# Home page
	url(r'^$', views.index, name='index'),
]