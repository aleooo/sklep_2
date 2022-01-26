import urllib
from django import template
from django.http import QueryDict

register = template.Library()

@register.filter
def urlquery(kwargs):
    if 'page' in kwargs:
        kwargs = dict(kwargs)
        del kwargs['page']
        kwargs = {k:v[0] for k, v in kwargs.items()}
    return '&' + urllib.parse.urlencode(kwargs)