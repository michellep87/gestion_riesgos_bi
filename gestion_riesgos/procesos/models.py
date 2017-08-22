from __future__ import unicode_literals

from django.db import models
from administracion.models import *
from .models import *
# -*- coding: utf-8 -*-
# Create your models here.

class Procesos(models.Model):
    codproceso = models.AutoField(db_column='CodProceso', primary_key=True)  # Field name made lowercase.
    codtipoproceso = models.ForeignKey(Tipoproceso, models.DO_NOTHING, db_column='CodTipoProceso', blank=True, null=True)  # Field name made lowercase.
    nombre_proceso = models.CharField(db_column='NombreProceso', max_length=75, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    idduenoproceso = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='IdDuenoProceso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    fecha_implementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'Procesos'
    def __unicode__(self):
        return u'%s' % (self.nombre_proceso)

class Subprocesos(models.Model):
    codsubproceso = models.AutoField(db_column='CodSubproceso', primary_key=True)  # Field name made lowercase.
    codproceso = models.ForeignKey(Procesos, models.DO_NOTHING, db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    descsubproceso = models.TextField(db_column='DescSubProceso', blank=True, null=True)  # Field name made lowercase.
    due_osubproceso = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='DuenoSubProceso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    orden_subproceso = models.IntegerField(db_column='OrdenSubproceso', blank=True, null=True)  # Field name made lowercase.
    diagrama = models.BinaryField(db_column='Diagrama', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    anexo = models.CharField(db_column='Anexo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    codestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='CodEstado', blank=True, null=True)  # Field name made lowercase.
    fecha_implementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubProcesos'
    def __unicode__(self):
        return u'%s - %s' % (self.codproceso, self.descsubproceso)

class Subprocesosxescenarios(models.Model):
    codsubprocesosxescenarios = models.AutoField(db_column='CodSubProcesosXEscenarios', primary_key=True)  # Field name made lowercase.
    codescenarioriesgo = models.ForeignKey(Escnariosriesgos, models.DO_NOTHING, db_column='CodEscenarioRiesgo', blank=True, null=True)  # Field name made lowercase.
    codsubproceso = models.ForeignKey(Subprocesos, models.DO_NOTHING, db_column='CodSubproceso', blank=True, null=True)  # Field name made lowercase.
    probabilidad = models.IntegerField(db_column='Probabilidad', blank=True, null=True)  # Field name made lowercase.
    impacto = models.IntegerField(db_column='Impacto', blank=True, null=True)  # Field name made lowercase.
    nivel_riesgo_inherente = models.IntegerField(db_column='NivelRiesgoInherente', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubProcesosXEscenarios'
    def __unicode__(self):
        return u'%s - %s' % (self.codsubproceso, self.codescenarioriesgo)



class Actividades(models.Model):
    codactividad = models.AutoField(db_column='CodActividad', primary_key=True)  # Field name made lowercase.
    codsubproceso = models.ForeignKey(Subprocesos, models.DO_NOTHING, db_column='CodSubproceso', blank=True, null=True)  # Field name made lowercase.
    ordenactividad = models.IntegerField(db_column='OrdenActividad', blank=True, null=True)  # Field name made lowercase.
    codtipoactividad = models.ForeignKey(Tipoactividad, models.DO_NOTHING, db_column='CodTipoActividad', blank=True, null=True)  # Field name made lowercase.
    descripcionactividad = models.TextField(db_column='DescripcionActividad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Actividades'
    def __unicode__(self):
        return u'%s' % (self.descripcionactividad)



class Raci(models.Model):
    idraci = models.AutoField(db_column='IdRaci', primary_key=True)  # Field name made lowercase.
    codactividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='CodActividad', blank=True, null=True)  # Field name made lowercase.
    codraci = models.ForeignKey(Tiporaci, models.DO_NOTHING, db_column='CodRaci', blank=True, null=True)  # Field name made lowercase.
    codpuesto = models.IntegerField(db_column='CodPuesto', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RACI'



















