var  x = new XMLHttpRequest();
var to = $('#list_input_to')
var from = $('#list_input_from')
var form_price = $('#list_form_price')
var pagination = $('.pagination_a').prop("selectedIndex", 0)
var slice = ''


if (location.href.includes('filter') == true || location.href.includes('from')) {

    
    if(location.href.includes('page')){
        slice = location.href.slice(0, location.href.search('page=')+5)
        if($('#list_laquo').length){
            $('#list_laquo').attr('href', slice + '1')
        }
        if($('#list_raquo').length){
            $('#list_raquo').attr('href', slice + $('#list_raquo')[0]['name'])    
        }
        pagination.each(function (index) {
            $(this).attr('href', slice + $(this)[0]['text'])
          })




    }
    else{
        pagination.attr('href', location.href.concat('&page=', pagination[0]['text']))
        $('#list_raquo').attr('href', location.href.concat('&page=', $('#list_raquo')[0]['name']))
    }
    
}

let number_from = ''
let number_to = ''
let form_price_action = location.pathname
form_price.attr("action", form_price_action)


to.keyup(w => { 
    number_from = w.target.value
    form_price_action =  location.pathname+'?from='+number_from+'&to='+number_to+'&'
    form_price.attr("action", form_price_action)
});
from.keyup(w => { 
    number_to = w.target.value
    form_price_action =  location.pathname+'?from='+number_from+'&to='+number_to+'&'
    form_price.attr("action", form_price_action)
    console.log(form_price_action)
});

