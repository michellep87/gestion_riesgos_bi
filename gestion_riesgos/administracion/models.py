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
        return u'%s' % (self.descripcion)

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
    descescenario = models.CharField(db_column='DescEscenario', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscnariosRiesgos'
    def __unicode__(self):
        return u'%s' % (self.descescenario)  

















