from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^procesos/ingreso/$', views.procesos, name= 'procesos'),
	url(r'^procesos/editar/(?P<id>.+)/$', views.procesos_editar, name= 'procesos_editar'),
	# url(r'^procesos/listado/$', views.procesos_listado, name= 'procesos_listado'),
	url(r'^procesos/subprocesos/ingreso/(?P<id>.+)/$', views.subprocesos, name= 'subprocesos'),

	#Ajax
	url(r'^ajaxproceso/$', views.ajaxproceso, name='ajaxproceso'),
]