from django import template

register = template.Library()

@register.filter
def index(queryset, value):
    
    try:
        object = queryset[value]
    except IndexError:
        object = ''
    
    if object:
        object = object.name
    
    return object
    
