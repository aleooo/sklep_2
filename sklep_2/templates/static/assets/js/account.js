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
function address(data, value=null, type){
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


    if(data.length > 50){
        data = JSON.parse(data);
        form_html = '';
        for (key in data){
            if(data[key].value.includes('no') || data[key].value.includes('brak')){
                data[key].value = '';
            }
            console.log(key);
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
            <input type="text" class="form-control font_numbers" id="floatingInput" placeholder="${value}" name="${data}" value="${value}">
            <label for="floatingInput">${data}</label></div>`)
    }
}
