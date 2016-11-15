import graphene

import apps.calendar.schema


class Query(
        apps.calendar.schema.DayQuery,
        apps.calendar.schema.CalendarQuery,
        graphene.ObjectType
        ):
    pass


schema = graphene.Schema(query=Query)
