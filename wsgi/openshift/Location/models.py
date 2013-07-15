from django.db import models
from django.db.models import Model
from Social.models import ActiveEntity, Nomenclator
from Contact.models import ContactItem


class Province(Nomenclator):
    pass


class Municipality(Nomenclator):
    province = models.ForeignKey(Province)


class Address(Model):
    street = models.CharField(max_length=256)
    locality = models.CharField(max_length=50)
    municipality = models.ForeignKey(Municipality)
    zip = models.IntegerField(max_length=5)


class Location(Model):
    name = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.FloatField()
    owner = models.ForeignKey(ActiveEntity)
    address = models.OneToOneField(Address)
    phone = models.OneToOneField(ContactItem)


