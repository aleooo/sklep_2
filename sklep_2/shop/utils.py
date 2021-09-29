def price_range_products(*args, **kwargs):
    filter = args[0].GET.get('filter')
    if filter:
        filter = int(filter)
        if filter == 20:
            return args[1].filter(price__lt=filter)
        elif filter == 50:
            return args[1].filter(price__range=(20, 50))
        elif filter == 75:
            return args[1].filter(price__range=(50, 75))
        elif filter == 150:
            return args[1].filter(price__range=(75, 150))
        else:
            return args[1].filter(price__range=(150, 1000000))
    else:
        return args[1]