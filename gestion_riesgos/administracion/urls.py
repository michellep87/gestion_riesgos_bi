from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^administracion/menu/$', views.menu_administracion, name= 'menu_administracion'),
	url(r'^administracion/tipo_area_ingreso/$', views.tipo_area, name= 'tipo_area'),
	url(r'^administracion/tipo_area_editar/(?P<id>.+)/$', views.tipo_area_editar, name= 'tipo_area_editar'),
	url(r'^administracion/areas_ingreso/$', views.areas, name= 'areas'),
	url(r'^administracion/areas_editar/(?P<id>.+)/$', views.areas_editar, name= 'areas_editar'),
	url(r'^administracion/puestos_ingreso/$', views.puestos, name= 'puestos'),
	url(r'^administracion/puestos_editar/(?P<id>.+)/$', views.puestos_editar, name= 'puestos_editar'),
	url(r'^administracion/tipo_proceso_ingreso/$', views.tipoproceso, name = 'tipoproceso'),
	url(r'^administracion/tipo_proceso_editar/(?P<id>.+)/$', views.tipoproceso_editar, name = 'tipoproceso_editar'),
	url(r'^administracion/tipo_actividad_ingreso/$', views.tipoactividad, name = 'tipoactividad'),
	url(r'^administracion/tipo_actividad_editar/(?P<id>.+)/$', views.tipoactividad_editar, name = 'tipoactividad_editar'),
	url(r'^administracion/tipo_control_ingreso/$', views.tipocontrol, name = 'tipocontrol'),
	url(r'^administracion/tipo_control_editar/(?P<id>.+)/$', views.tipocontrol_editar, name = 'tipocontrol_editar'),
	url(r'^administracion/tipo_raci_ingreso/$', views.tiporaci, name = 'tiporaci'),
	url(r'^administracion/tipo_raci_editar/(?P<id>.+)/$', views.tiporaci_editar, name = 'tiporaci_editar'),
	url(r'^administracion/tipo_riesgos_ingreso/$', views.tiporiesgos, name = 'tiporiesgos'),
	url(r'^administracion/tipo_riesgos_editar/(?P<id>.+)/$', views.tiporiesgos_editar, name = 'tiporiesgos_editar'),
	url(r'^administracion/riesgos_ingreso/$', views.riesgos, name = 'riesgos'),
	url(r'^administracion/riesgos_editar/(?P<id>.+)/$', views.riesgos_editar, name = 'riesgos_editar'),
	url(r'^administracion/naturaleza_control_ingreso/$', views.naturalezacontrol, name = 'naturalezacontrol'),
	url(r'^administracion/naturaleza_control_editar/(?P<id>.+)/$', views.naturalezacontrol_editar, name = 'naturalezacontrol_editar'),
	url(r'^administracion/escenario_riesgos_ingreso/$', views.escenarioriesgos, name = 'escenarioriesgos'),
	url(r'^administracion/escenario_riesgos_editar/(?P<id>.+)/$', views.escenarioriesgos_editar, name = 'escenarioriesgos_editar'),
	url(r'^ajax/$', views.ajax, name='ajax'),

]
