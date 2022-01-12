from django import template


register = template.Library()



@register.filter
def price_front(value):
    value = str(value)
    front = value.split('.')[0]
    return front

@register.filter
def price_back(value):
    print(value)
    value = str(value)
    back = value.split('.')[1]
    if len(back) < 2:
        back +=(len(back) * '0') 
    back = '.' + back
    return back

