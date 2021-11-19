let plus = $('#plus')
let minus = $('#minus')
let input = $('#input')
let box_info_added_product = $('#box_info_added_product')


    
plus.click(function(){
    input.val(parseInt(input.val()) + 1 );
        });
minus.click(function(){
    input.val(parseInt(input.val()) - 1 );
if (input.val() == 0) {
    input.val(1);
}});


window.onclick = function(e){
        
        if(e.target.id != 'box_info'){
            box_info_added_product.css('display', 'none');
        }
}



