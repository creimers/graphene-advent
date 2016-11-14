from django.contrib import admin

from image_cropping import ImageCroppingMixin

from .models import Calendar, Day


class DayInline(ImageCroppingMixin, admin.StackedInline):
    model = Day
    extra = 1
    # TODO: dynamically determine how many extras... 1 or 0.


class CalendarAdmin(admin.ModelAdmin):
    inlines = [DayInline, ]
    readonly_fields = ('uuid', )


admin.site.register(Calendar, CalendarAdmin)
