from django.db import models
from django.db.models import Model
from Social.models import ActiveEntity, Nomenclator


class ContactType(Nomenclator):
    regEx = models.CharField(max_length=120)


class ContactItem(Model):
    type = models.ForeignKey(ContactType)
    owner = models.ForeignKey(ActiveEntity)
    value = models.CharField(max_length=100)



