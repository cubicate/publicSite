from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.db.models.signals import post_save


VISIBILITY_LEVELS = (
    (u'prv', u'Private'),
    (u'flw', u'Followers'),
    (u'pub', u'Public'),
)


class Nomenclator(Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5)

    class Meta:
        abstract = True


class PlaceCategory(Nomenclator):
    pass


class PlaceFeature(Nomenclator):
    pass


class ActiveEntity(Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    avatar = models.ImageField(upload_to='avatars')
    defaultVisibility = models.CharField(max_length=5, choices=VISIBILITY_LEVELS, default='pub')
    followers = models.ManyToManyField(User, through='Follow')


class Place(ActiveEntity):
    description = models.TextField()
    category = models.ForeignKey(PlaceCategory)
    features = models.ManyToManyField(PlaceFeature)
    likes = models.IntegerField()
    totalVisits = models.IntegerField()
    visitors = models.ManyToManyField(User, related_name='visitedPlaces')
    ratings = models.ManyToManyField(User, through='Rating', related_name='ratedPlaces')


class ActiveContent(Model):
    visibility = models.CharField(max_length=5, choices=VISIBILITY_LEVELS)
    entity = models.ForeignKey(ActiveEntity)
    creationDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    references = models.ManyToManyField('self', symmetrical=False)


class Review(ActiveContent):
    multiple = models.BooleanField(default=False)
    places = models.ManyToManyField(Place)


class Announcement(ActiveContent):
    IMPORTANCE_LEVEL = (
        (1, u'Not important'),
        (2, u'Important'),
        (3, u'Very important'),
    )
    importance = models.IntegerField(max_length=2, choices=IMPORTANCE_LEVEL)
    availableDate = models.DateTimeField()


class Rating(Model):
    RATES = (
        (1, u'I hated it'),
        (2, u'I don\'t liked'),
        (3, u'I liked'),
        (4, u'I really liked'),
        (5, u'I loved it'),
    )
    user = models.ForeignKey(User)
    place = models.ForeignKey(Place)
    rate = models.IntegerField(max_length=2, choices=RATES)


class Follow(Model):
    user = models.ForeignKey(User)
    entity = models.ForeignKey(ActiveEntity)
    since = models.DateTimeField(auto_now_add=True)
    reviews = models.BooleanField(default=True)
    contentUpdates = models.BooleanField(default=True)
    comments = models.BooleanField(default=True)


class UserProfile(ActiveEntity):
    user = models.OneToOneField(User)
    GENDER = (
        (u'male', u'Male'),
        (u'female', u'Female'),
    )
    sex = models.CharField(max_length=8, choices=GENDER)
    birthDate = models.DateField()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)