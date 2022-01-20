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

(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()
