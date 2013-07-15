from django.db import models
from django.db.models import Model


class DayHours(Model):
    WEEK_DAYS = (
        (u'mon', u'Monday'),
        (u'tue', u'Tuesday'),
        (u'wed', u'Wednesday'),
        (u'thu', u'Thursday'),
        (u'fri', u'Friday'),
        (u'sat', u'Saturday'),
        (u'sun', u'Sunday'),
    )
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=256)
    weekDay = models.CharField(max_length=5, choices=WEEK_DAYS, null=True)
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