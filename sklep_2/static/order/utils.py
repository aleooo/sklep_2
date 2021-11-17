def data(user):
    data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone_number': user.number
        }
    if user.address:
        address = user.address
        data_address = {
            'street': address.street,
            'street_number': address.street_number,
            'ZIP_code': address.ZIP_code,
            'town': address.town,
            'country': address.country
        }
        data = {**data, **data_address}
    return data