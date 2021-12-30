var password = document.getElementById("password1")
  , confirm_password = document.getElementById("password2");



function validatePassword(){
  
  if($('#password1').val.length >= 8){
    $('#password_minlength')
    console.log(8);
  }
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Invalid");
  } else {
    confirm_password.setCustomValidity('');
  }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;


