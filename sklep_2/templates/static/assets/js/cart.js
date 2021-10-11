var plus = $('#plus')
var minus = $('#minus')
var input = $('#input')
var plus_media = $('#pluss')
var minus_media = $('#minuss')
var input_media = $('#inputt')
var for_each = $('#for_each')

plus.click(function(){
    input.val(parseInt(input.val()) + 1 );
        });
minus.click(function(){
    input.val(parseInt(input.val()) - 1 );
if (input.val() == 0) {
    input.val(1);
}});

show_for_each()
plus_media.click(function(){
    show_for_each()
    input_media.val(parseInt(input_media.val()) + 1 );
    show_for_each()
        });
minus_media.click(function(){
    input_media.val(parseInt(input_media.val()) - 1 );
    show_for_each()
if (input_media.val() == 0) {
    input_media.val(1);
}});
function show_for_each(){
    if (input_media.val() < 2){
        console.log(1)
        for_each.css('display', 'none')
    }
    else{
        for_each.css('display', 'block')
    }
}

