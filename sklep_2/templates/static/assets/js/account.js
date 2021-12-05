background = $('#account_background_form')
div_form = $('#account_div_form')
form = $('#account_form')
addresses = {'ZIP_code': 'ZIP code',
            'street': 'Street',
            'street_number': 'Street number',
            'town': 'Town',
            'country': 'Country'}


// cancel form address and personal data
function cancel(){
    background.css('display', 'none')
    div_form.css('display', 'none')
    
}

// call form to set address fields
function address(value){
    background.css('display', 'block')
    div_form.css('display', 'block')
    
    form.html(`<form action="" class="form-floating mb-3"><input type="email" class="form-control" id="floatingInput" placeholder="name@example.com"><label for="floatingInput">${addresses[value]}</label></form>`)
    
}