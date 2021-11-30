from django import template


register = template.Library()



@register.filter
def price_front(value):
    value = str(value)
    return value[:-3]

@register.filter
def price_back(value):
    value = str(value)
    return value[-3:]

