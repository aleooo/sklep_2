let plus = $('#plus')
let minus = $('#minus')
let input = $('#input')
let a = $('.but')
var error = sessionStorage.getItem('error')
var add = sessionStorage.getItem('add')

    
plus.click(function(){
    input.val(parseInt(input.val()) + 1 );
        });
minus.click(function(){
    input.val(parseInt(input.val()) - 1 );
if (input.val() == 0) {
    input.val(1);
}});


if (add){
    console.log(add)
    sessionStorage.setItem('add', false)
}
if (error){
    console.log(error)
    sessionStorage.setItem('error', false)
}

