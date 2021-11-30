var for_each = $('#for_each')

function show_for_each(){
    if (input_media.val() < 2){
        for_each.css('display', 'none')
    }
    else{
        for_each.css('display', 'block')
    }
};

function plus(id){
    input = $('.input'+id)
    input.val(parseInt(input.val())+1)
};
function minus(id){
    input = $('.input'+id)
    if (input.val() > 1){
        input.val(parseInt(input.val())-1)
    }
};
