from django.db import models

import datetime

from easy_thumbnails.files import get_thumbnailer

from filer.fields.image import FilerImageField

import shortuuid


class Calendar(models.Model):

    name = models.CharField(max_length=250)
    uuid = models.CharField(max_length=22)
    YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year+1)]
    year = models.IntegerField(
        null=True, max_length=4, choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
        )

    def create_uuid(self):
        return shortuuid.uuid()

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = self.create_uuid()
        super(Calendar, self).save(*args, **kwargs)

    def existing_days(self):
        return self.days.all().count()

    def __str__(self):
        return self.name


class Day(models.Model):
    class Meta:
        unique_together = (('day', 'calendar'))
        ordering = ['day', ]

    calendar = models.ForeignKey(Calendar, related_name="days")

    DAY_CHOICES = lambda x: [(i, '_' + str(i) + '_') for i in range(1, x + 1)]
    day = models.IntegerField(choices=DAY_CHOICES(24))
    image_source = models.URLField(blank=True)

    original_image = FilerImageField(null=True)

    def get_image_small_url(self):
        # TODO: get these from the field
        height = 400
        width = 400
        return get_thumbnailer(self.original_image.file).get_thumbnail({
            'size': (width, height),
            'crop': True,
            'upscale': True,
            'detail': True,
            'subject_location': self.original_image.subject_location
            }).url

    def get_image_large_url(self):
        # TODO: get these from the field
        height = 1200
        width = 1200
        return get_thumbnailer(self.original_image.file).get_thumbnail({
            'size': (width, height),
            'crop': True,
            'upscale': True,
            'detail': True,
            'subject_location': self.original_image.subject_location
            }).url

    def __str__(self):
        return ' '.join([self.calendar.name, str(self.day)])
