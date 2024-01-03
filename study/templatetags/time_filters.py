# from django import template
# from django.utils.timesince import timesince

# register = template.Library()

# @register.filter
# def humanize_time(timestamp):
#     return timesince(timestamp)


from django import template
from django.utils.timesince import timesince
from django.utils.timezone import now
import datetime

register = template.Library()

@register.filter(name='time_ago')
def time_ago(value):
    if isinstance(value, datetime.datetime):
        return timesince(value, now())
    return value  # Return the original value if it's not a datetime object




# from django import template
# from django.utils.timesince import timesince
# from django.utils.timezone import now

# register = template.Library()

# @register.filter(name='time_ago')
# def time_ago(value):
#     return timesince(value, now())

