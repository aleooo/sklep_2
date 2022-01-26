// var  x = new XMLHttpRequest();
// var to = $('#list_input_to')
// var from = $('#list_input_from')
// var form_price = $('#list_form_price')
// var pagination = $('.pagination_a').prop("selectedIndex", 0)
// var filter_button = $('#list_filter')
// var slice = ''
// let number_from = ''
// let number_to = ''
// let form_price_action = location.pathname

// // in the case of a filter, the href of the paging buttons would not redirect to the filter page
// // checks if the url has any filter keywords 
// if (location.href.includes('filter') == true || location.href.includes('from')) {

//     if(location.href.includes('page')){

//         // slice from url, for example url: http://127.0.0.1:8000/en/list/search/i/?page=2 will be slice http://127.0.0.1:8000/en/list/search/i/?page=
//         slice = location.href.slice(0, location.href.search('page=')+5)
//         if($('#list_laquo').length){
//             $('#list_laquo').attr('href', slice + '1')
//         }
//         if($('#list_raquo').length){
//             $('#list_raquo').attr('href', slice + $('#list_raquo')[0]['name'])    
//         }
//         pagination.each(function (index) {
//             $(this).attr('href', slice + $(this)[0]['text'])
//           })
//     }
//     else{
//         // if there is more than one page
//         if(pagination.length > 0){

//             // assign href to the next button after the current one that redirects to the filter page
//             pagination.attr('href', location.href.concat('&page=', pagination[0]['text']))
//             // assign href to the raquo that redirects to the next filter page
//             $('#list_raquo').attr('href', location.href.concat('&page=', $('#list_raquo')[0]['name']))
//         }
//     }   
// }


// form_price.attr("action", form_price_action)


// to.keyup(w => { 
//     number_from = w.target.value
//     form_price_action =  location.pathname+'?from='+number_from+'&to='+number_to+'&'
//     form_price.attr("action", form_price_action)
// });
// from.keyup(w => { 
//     number_to = w.target.value
//     form_price_action =  location.pathname+'?from='+number_from+'&to='+number_to+'&'
//     form_price.attr("action", form_price_action)
// });


function list_filter_button(){
    filter_button.css('display', 'block')
}
