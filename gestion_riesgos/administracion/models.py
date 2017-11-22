# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from procesos.models import *


# Create your models here.


class Tipoareas(models.Model):
    codtipoarea = models.AutoField(db_column='CodTipoArea', primary_key=True)  # Field name made lowercase.
    desctipoarea = models.CharField(db_column='DescTipoArea', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoAreas'
    def __unicode__(self):
        return u'%s' % (self.desctipoarea)

class Tipoproceso(models.Model):
    codtipoproceso = models.AutoField(db_column='CodTipoProceso', primary_key=True)  # Field name made lowercase.
    desctipoproceso = models.CharField(db_column='DescTipoProceso', max_length=75, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TipoProceso'

    def __unicode__(self):
        return u'%s' % (self.desctipoproceso)   

class Tipoactividad(models.Model):
    codtipoactividad = models.AutoField(db_column='CodTipoActividad', primary_key=True)  # Field name made lowercase.
    desctipoactividad = models.CharField(db_column='DescTipoActividad', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoActividad'
    def __unicode__(self):
        return u'%s' % (self.desctipoactividad)     

class Tipocontrol(models.Model):
    codtipocontrol = models.AutoField(db_column='CodTipoControl', primary_key=True)  # Field name made lowercase.
    desctipocontrol = models.CharField(db_column='DescTipoControl', max_length=150, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TipoControl'
    def __unicode__(self):
        return u'%s' % (self.desctipocontrol)


class Tiporaci(models.Model):
    codraci = models.AutoField(db_column='CodRaci', primary_key=True)  # Field name made lowercase.
    letra = models.CharField(db_column='Letra', max_length=1, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoRACI'
    def __unicode__(self):
        return u'%s' % (self.letra)

class Tiposriesgos(models.Model):
    codtiporiesgo = models.AutoField(db_column='CodTipoRiesgo', primary_key=True)  # Field name made lowercase.
    desctiporiesgo = models.CharField(db_column='DescTipoRiesgo', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposRiesgos'
    def __unicode__(self):
        return u'%s' % (self.desctiporiesgo)

class Estados(models.Model):
    codestado = models.AutoField(db_column='CodEstado', primary_key=True)  # Field name made lowercase.
    descestado = models.CharField(db_column='DescEstado', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estados'
    def __unicode__(self):
        return u'%s' % (self.descestado)

class Naturalezacontrol(models.Model):
    codnaturaleza = models.AutoField(db_column='CodNaturaleza', primary_key=True)  # Field name made lowercase.
    descnaturaleza = models.CharField(db_column='DescNaturaleza', max_length=150, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'NaturalezaControl'

class Areas(models.Model):
    codarea = models.AutoField(db_column='CodArea', primary_key=True)  # Field name made lowercase.
    descarea = models.CharField(db_column='DescArea', max_length=75, blank=True, null=True)  # Field name made lowercase.
    codtipoarea = models.ForeignKey('Tipoareas', models.DO_NOTHING, db_column='CodTipoArea', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Areas'
    def __unicode__(self):
        return u'%s' % (self.descarea)


class Puestos(models.Model):
    codpuesto = models.AutoField(db_column='CodPuesto', primary_key=True)  # Field name made lowercase.
    codarea = models.ForeignKey('Areas', models.DO_NOTHING, db_column='CodArea', blank=True, null=True)  # Field name made lowercase.
    descpuesto = models.CharField(db_column='DescPuesto', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Puestos'
    def __unicode__(self):
        return u'%s' % (self.descpuesto)

class Riesgos(models.Model):
    codriesgo = models.AutoField(db_column='CodRiesgo', primary_key=True)  # Field name made lowercase.
    codtiporiesgo = models.ForeignKey('Tiposriesgos', models.DO_NOTHING, db_column='CodTipoRiesgo', blank=True, null=True)  # Field name made lowercase.
    descriesgo = models.CharField(db_column='DescRiesgo', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Riesgos'
    def __unicode__(self):
        return u'%s' % (self.descriesgo)    



class Escnariosriesgos(models.Model):
    codescenarioriesgo = models.AutoField(db_column='CodEscenarioRiesgo', primary_key=True)  # Field name made lowercase.
    codriesgo = models.ForeignKey(Riesgos, models.DO_NOTHING, db_column='CodRiesgo', blank=True, null=True)  # Field name made lowercase.
    descescenario = models.TextField(db_column='DescEscenario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscnariosRiesgos'
    def __unicode__(self):
        return u'%s' % (self.descescenario)  


class Empleados(models.Model):
    empleado = models.AutoField(db_column='CodEmpleado', primary_key=True)  # Field name made lowercase.
    nombre_completo = models.CharField(db_column='NombreCompleto', max_length=75, blank=True, null=True)  # Field name made lowercase.
    usuarioad = models.CharField(db_column='UsuarioAD', max_length=75, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=75, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=75, blank=True, null=True)  # Field name made lowercase.
    fecha_ingreso = models.DateTimeField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empleados'        

class EmpleadoxAreas(models.Model):
    empleadoarea = models.AutoField(db_column='CodEmpeladoXArea', primary_key=True)  # Field name made lowercase.
    area = models.ForeignKey(Areas, models.DO_NOTHING, db_column='CodArea', blank=True, null=True)  # Field name made lowercase.
    empleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='CodEmpleado', blank=True, null=True)  # Field name made lowercase.
    fecha_inicio = models.DateTimeField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fecha_final = models.DateTimeField(db_column='FechaFinal', blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmpleadoXAreas'


class CategoriaRiesgos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codcategoria = models.CharField(db_column='CodCategoria', max_length=20, blank=True, null=True) 
    descripcion = models.CharField(db_column='DescripcionCategoria', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoriaRiesgos'
    def __unicode__(self):
        return u'%s - %s' % (self.codcategoria,self.descripcion)  


class AreasInvolucradas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescripcionAreasInvolucradas', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AreasInvolucradas'
    def __unicode__(self):
        return u'%s' % (self.descripcion)  

class CumplimientoNormativo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescripcionCumplimientoNormativo', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CumplimientoNormativo'
    def __unicode__(self):
        return u'%s' % (self.descripcion)    

class DefinicionProceso(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescripcionDefinicionProceso', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DefinicionProceso'
    def __unicode__(self):
        return u'%s' % (self.descripcion)

class EventosRiesgo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescripcionEventoRiesgo', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventosRiesgo'
    def __unicode__(self):
        return u'%s' % (self.descripcion)

class FrecuenciaActividadesRelacionadasRiesgo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescripcionFrecuencia', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FrecuenciaActividadesRelacionadasRiesgo'
    def __unicode__(self):
        return u'%s' % (self.descripcion)


class FrecuenciaControl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescripcionFrecuenciaControl', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FrecuenciaControl'
    def __unicode__(self):
        return u'%s' % (self.descripcion)

class ObservacionesAuditoria(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescripcionObservacionesAuditoria', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObservacionesAuditoria'
    def __unicode__(self):
        return u'%s' % (self.descripcion)

class Puntajescriterioscontrol(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=200)  # Field name made lowercase.
    puntaje = models.DecimalField(db_column='Puntaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PuntajesCriteriosControl'

class PuntajesCriteriosImpacto(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=200)  # Field name made lowercase.
    puntaje = models.DecimalField(db_column='Puntaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PuntajesCriteriosImpacto'



class PuntajesCriteriosProbabilidad(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=200)  # Field name made lowercase.
    puntaje = models.DecimalField(db_column='Puntaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PuntajesCriteriosProbabilidad'


class RiesgoInstitucional(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescripcionRiesgoInstitucional', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RiesgoInstitucional'
    def __unicode__(self):
        return u'%s' % (self.descripcion)


class RiesgoReputacional(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescripcionRiesgoRepudial', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RiesgoReputacional'
    def __unicode__(self):
        return u'%s' % (self.descripcion)

class TransaccionesEstadosFinancieros(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DescripcionTransaccionesEstadosFinancieros', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransaccionesEstadosFinancieros'
    def __unicode__(self):
        return u'%s' % (self.descripcion)

class Escalaimpacto(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscalaImpacto'


class Escalaprobabilidad(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscalaProbabilidad'
    def __unicode__(self):
        return u'%s' % (self.clasificacion)

class EscalaControl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscalaControl'
    def __unicode__(self):
        return u'%s' % (self.clasificacion)

class Zonariesgo(models.Model):
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZonaRiesgo'
    def __unicode__(self):
        return u'%s' % (self.clasificacion)




















