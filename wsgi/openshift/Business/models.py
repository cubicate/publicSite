from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from Social.models import Place, Nomenclator


class BusinessType(Nomenclator):
    parent = models.ForeignKey('self', related_name='childs')
    description = models.TextField()


class PaymentType(Nomenclator):
    pass


class Business(Place):
    slogan = models.CharField(max_length=256)
    owner = models.ForeignKey(User)
    managers = models.ManyToManyField(User, related_name='managedBusiness')
    type = models.ForeignKey(BusinessType)
    accepts = models.ManyToManyField(PaymentType)