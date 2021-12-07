var background = $('#account_background_form')
var div_form = $('#account_div_form')
var form_address = $('#account_form_address')
var form_personal_data = $('#account_form_personal_data')
var account_div_form_address = $('#account_div_form_address')
var account_div_form_personal_data = $('#account_div_form_personal_data')
var tag_form = $('#account_tag_form')


// cancel form address and personal data
function cancel(){
    background.css('display', 'none');
    div_form.css('display', 'none');
    account_div_form_address.css('display', 'none');
    account_div_form_personal_data.css('display', 'none');
    form_address.html('');
    form_personal_data.html('');
}

// call a form to the address and personal data user
function account_form(data, type, kind=null){
    data = JSON.parse(data);
    form_html = '';

    background.css('display', 'block');
    div_form.css('display', 'block');
    
    if(type == 'address'){
        account_div_form_address.css('display', 'block')
        var form = form_address
    }
    else if(type == 'personal_data'){
        account_div_form_personal_data.css('display', 'block')
        var form = form_personal_data
    }
    
    if(kind){
        form_html = `<div class="form-floating mb-3">
            <input type="text" class="form-control font_numbers_light" id="floatingInput" placeholder="${data[kind].field}" name="${data[kind].name}" value="${data[kind].value}">
            <label for="floatingInput">${data[kind].field}</label></div>`
    }
    else{
        for (kind in data){
            form_html += `<div class="form-floating mb-3">
                            <input type="text" class="form-control font_numbers_light" id="${data[kind].name}_input" placeholder="${data[kind].field}" name="${data[kind].name}" value="${data[kind].value}">
                            <label for="${data[kind].name}_input">${data[kind].field}</label>
                            </div>`
            }
        
    }
    form.html(form_html)
}
