from graphene import relay, AbstractType, String
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Calendar, Day


class CalendarNode(DjangoObjectType):
    """
    how does this work?
    """
    class Meta:
        model = Calendar
        filter_fields = {
            'uuid': ['exact', ]
            }
        interfaces = (relay.Node, )


class CalendarQuery(AbstractType):
    """
    how does this work?
    """
    calendar = relay.Node.Field(CalendarNode)
    calendars = DjangoFilterConnectionField(CalendarNode)


class DayNode(DjangoObjectType):
    """
    how does this work?
    """
    class Meta:
        model = Day
        interfaces = (relay.Node, )
        exclude_fields = ('image', 'image_small', 'image_large')

    image_large_url = String()
    image_small_url = String()

    def resolve_image_large_url(self, args, context, info):
        """
        self is the Day instance
        """
        return DayNode.get_absolute_image_url(
            context, self.get_image_large_url()
        )

    def resolve_image_small_url(self, args, context, info):
        """
        self is the Day instance
        """
        return DayNode.get_absolute_image_url(
            context, self.get_image_small_url()
        )

    def get_absolute_image_url(context, relative_url):
        return context.scheme + '://' + context.get_host() + relative_url


class DayQuery(AbstractType):
    """
    how does this work?
    """
    day = relay.Node.Field(DayNode)
    days = DjangoFilterConnectionField(DayNode)
