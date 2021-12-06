background = $('#account_background_form')
div_form = $('#account_div_form')
form = $('#account_form')
addresses = {
            'town': 'Town',
            'ZIP_code': 'ZIP code',
            'country': 'Country',
            'street_number': 'Street number',
            'street': 'Street',}


// cancel form address and personal data
function cancel(){
    background.css('display', 'none')
    div_form.css('display', 'none')
    
}

// call form to set address fields
function address(value){
    background.css('display', 'block')
    div_form.css('display', 'block')
    if(value == 'all'){
        for ([key, value] of Object.entries(addresses)){
            form.prepend(`
            <div class="form-floating mb-3">
                <input type="text" class="form-control" id="${key}_input" placeholder="${value}" name="${key}">
                <label for="${key}_input">${value}</label>
            </div>`)
        };
    }
    else{
        form.prepend(`
        <div class="form-floating mb-3">
            <input type="text" class="form-control" id="floatingInput" placeholder="${addresses[value]}" name="${value}">
            <label for="floatingInput">${addresses[value]}</label>
        </div>`)
    }
    
    
}