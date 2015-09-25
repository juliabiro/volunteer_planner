# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    '''
    A country
    '''
    name = models.CharField(max_length=50, unique=True, verbose_name=_('name'))
    slug = models.SlugField(verbose_name=_(u'slug'))

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')
        ordering = ('name',)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Region(models.Model):
    '''
    A region is a geographical region for grouping areas (and facilities within areas).
    '''
    name = models.CharField(max_length=50, unique=True, verbose_name=_('name'))
    country = models.ForeignKey(Country,
                                related_name='regions',
                                verbose_name=_('country'))
    slug = models.SlugField(verbose_name=_(u'slug'))

    class Meta:
        verbose_name = _('region')
        verbose_name_plural = _('regions')
        ordering = ('country', 'name',)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Area(models.Model):
    '''
    An area is a subdevision of a region, such as cities, neighbourhoods, etc.
    Each area belongs to a region.
    '''
    region = models.ForeignKey(Region, related_name='areas',
                               verbose_name=_('region'))
    name = models.CharField(max_length=50, unique=True, verbose_name=_('name'))
    slug = models.SlugField(verbose_name=_(u'slug'))

    class Meta:
        verbose_name = _('area')
        verbose_name_plural = _('areas')
        ordering = ('region', 'name',)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Municipality(models.Model):
    '''
    A municipality (german: Gemeinde) can be a city like Jena in Thüringen - Jena
    or a 'district' like  Wilmersdorf in Berlin - Berlin.
    '''
    area = models.ForeignKey(Area, related_name='municipalities',
                             verbose_name=_('municipality'))
    name = models.CharField(max_length=50, unique=True, verbose_name=_('name'))
    slug = models.SlugField(verbose_name=_(u'slug'))

    def __unicode__(self):
        return u'{}'.format(self.name)

    class Meta:
        verbose_name = _('municipality')
        verbose_name_plural = _('municipalities')
        ordering = ('area', 'name',)