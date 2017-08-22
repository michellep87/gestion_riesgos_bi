from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

	url(r'^$', views.login, name='login'),	
	url(r'^logout/$', views.cerrar_sesion, name='cerrar_sesion'),
	url(r'^menu/$', views.menu, name='menu'),  
]