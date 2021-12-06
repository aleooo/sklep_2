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
    form.html('')
    
}

// call form to set address fields
function address(data, value=null){
    
    background.css('display', 'block');
    div_form.css('display', 'block');
    if(data.length > 50){
        data = JSON.parse(data);
        form_html = '';
    
        for (key in data){
            if(data[key].value.includes('no') || data[key].value.includes('brak')){
                data[key].value = '';
            }
            
            form_html += `<div class="form-floating mb-3">
                            <input type="text" class="form-control" id="${key}_input" placeholder="${data[key]['field']}" name="${key}" value="${data[key].value}">
                            <label for="${key}_input">${data[key]['field']}</label>
                          </div>`
            }
       
        form.html(form_html)
        
    }
    else{
        if(value.includes('no') || value.includes('brak')){
            value = '';
        }
        form.html(`<div class="form-floating mb-3">
            <input type="text" class="form-control" id="floatingInput" placeholder="${value}" name="${data}" value="${value}">
            <label for="floatingInput">${data}</label></div>`)
    }
    
    
}