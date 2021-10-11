let plus = $('#plus')
let minus = $('#minus')
let input = $('#input')

plus.click(function(){
    console.log('plus')
    input.val(parseInt(input.val()) + 1 );
        });
minus.click(function(){
    input.val(parseInt(input.val()) - 1 );
if (input.val() == 0) {
    input.val(1);
}});