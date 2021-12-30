var password = document.getElementById("password1")
  , confirm_password = document.getElementById("password2");

function validatePassword(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
  } else {
    confirm_password.setCustomValidity('');
    console.log('same');
  }
}
$('#id_username').val('')
$('#id_password1').val('aaa')
password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;


