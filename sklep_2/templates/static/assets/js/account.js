var background = $('#account_background_form')
var div_form = $('#account_div_form')
var form_address = $('#account_form_address')
var form_personal_data = $('#account_form_personal_data')
var account_div_form_address = $('#account_div_form_address')
var account_div_form_personal_data = $('#account_div_form_personal_data')
var tag_form = $('#account_tag_form')
var personal_form_ids = ['first_name', 'last_name', 'email', 'phone_number']
var address_form_ids = ['street', 'street_number', 'town', 'ZIP_code', 'country']


// cancel form address and personal data
function cancel(type){
    for (personal_id of personal_form_ids){
        $(`#${personal_id}`).css('display', 'none');
    }
    for (address_id of address_form_ids){
        $(`#${address_id}`).css('display', 'none');
    }
    background.css('display', 'none');
    div_form.css('display', 'none');
    account_div_form_address.css('display', 'none');
    account_div_form_personal_data.css('display', 'none');


}

// call a form to the address and personal data user
function account_form(type, kind=null){
    background.css('display', 'block');
    div_form.css('display', 'block');
    
    if(type == 'address'){
        account_div_form_address.css('display', 'block')
        if (kind == 'all'){
            for (address_id of address_form_ids){
                $(`#${address_id}`).css('display', 'block')
            }
        }
        else{
            
            $(`#${kind}`).css('display', 'block')
  
        }
    }
    else if(type == 'personal_data'){
        account_div_form_personal_data.css('display', 'block')
        if (kind == 'all'){
            for (personal_id of personal_form_ids){
                $(`#${personal_id}`).css('display', 'block')
            }
        }
        else{
            
            $(`#${kind}`).css('display', 'block')
  
        }
    }

    
}

function none(){
    console.log('form alert');
}