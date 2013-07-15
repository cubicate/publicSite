from django.db import models
from django.db.models import Model


class DayHours(Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=256)
    openHours = models.ForeignKey('OpenHours', related_name='specialDayHours')


class OpenHours(Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=256)
    public = models.BooleanField(default=False)
    defaultDayHours = models.OneToOneField(DayHours)


class TimeRange(Model):
    form = models.TimeField()
    to = models.TimeField()
    dayHours = models.ForeignKey(DayHours)