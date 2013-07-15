from django.db import models
from django.db.models import Model
from libxml2mod import parent
from Social.models import ActiveContent, Nomenclator


class GalleryTemplate(Nomenclator):
    description = models.CharField(max_length=256)
    cssClass = models.CharField(max_length=64)


class Gallery(ActiveContent):
    parent = models.ForeignKey('self', related_name='children')
    template = models.ForeignKey(GalleryTemplate)