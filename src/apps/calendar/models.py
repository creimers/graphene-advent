from django.db import models

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

    calendar = models.ForeignKey(Calendar, related_name="days")

    DAY_CHOICES = lambda x: [(str(i), '_' + str(i)) for i in range(1, x + 1)]
    day = models.CharField(max_length=2, choices=DAY_CHOICES(24))
    image_source = models.URLField(blank=True)

    image = models.ImageField()
    image_small = ImageRatioField('image', '250x250')
    image_large = ImageRatioField('image', '1200x1200')

    def __str__(self):
        return ' '.join([self.calendar.name, self.day])
