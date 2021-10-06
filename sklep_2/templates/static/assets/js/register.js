let password1 = $('#id_password1')
let password2 = $('#id_password2')

function register() {
    password1.attr('placeholder', 'password')
    password2.attr('placeholder', 'password again')
  }


window.onload = register()

