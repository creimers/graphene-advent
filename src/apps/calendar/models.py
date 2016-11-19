from django.db import models

from easy_thumbnails.files import get_thumbnailer

from filer.fields.image import FilerImageField

from image_cropping import ImageRatioField

import shortuuid


class Calendar(models.Model):

    name = models.CharField(max_length=250)
    uuid = models.CharField(max_length=22)

    def create_uuid(self):
        return shortuuid.uuid()

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = self.create_uuid()
        super(Calendar, self).save(*args, **kwargs)

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
    image_small = ImageRatioField('original_image', '250x250')
    image_large = ImageRatioField('original_image', '1200x1200')

    def get_image_small_url(self):
        # TODO: get these from the field
        height = 400
        width = 400
        return get_thumbnailer(self.original_image.file).get_thumbnail({
            'size': (width, height),
            'box': self.image_small,
            'crop': True,
            'detail': True,
            }).url

    def get_image_large_url(self):
        # TODO: get these from the field
        height = 1200
        width = 1200
        return get_thumbnailer(self.original_image.file).get_thumbnail({
            'size': (width, height),
            'box': self.image_large,
            'crop': True,
            'detail': True,
            }).url

    def __str__(self):
        return ' '.join([self.calendar.name, str(self.day)])
