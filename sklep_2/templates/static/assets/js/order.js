


$("input[type=radio][name=delivery").click(elem => {
    if (elem.target.id == 'parcer_locker'){
        $('#map_parcel_locker').css('display', 'block')
    }
    else{
        $('#map_parcel_locker').css('display', 'none')
    }
})


var m = L.map('map_parcel_locker').setView([52.236, 21.022], 13)
  
// L.control.addTo(m);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYWxlb28iLCJhIjoiY2t5dDdzNXU2MWIyZDJ2bzNybjh5emdqMiJ9.PLVGGIqVXevnAjsguGZmYg'
}).addTo(m)

points = [
    ['Warsaw', ['52.241333', '21.028198']],
    ['Gdansk', [54.349722, 18.648001]],
    ['Cracow', [50.055142, 19.934230]],
]

for(i=0; i<points.length; i++){
    L.marker(points[i][1]).addTo(m).bindPopup(points[i][0]);
}
 
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
  