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


function parcels_map(markups){
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

  for(i=0; i<markups.length; i++){
    L.marker(markups[i][1]).addTo(m).bindPopup(markups[i][0]);
  }
}


function parcels_array(objects){
  let points = []
  for (parcel of objects){
    parc = [`${parcel.name}<br>${parcel.street} ${parcel.street_number}<br>${parcel.ZIP_code}<br>${parcel.town}<br>`, [parseFloat(parcel.latitude), parseFloat(parcel.longitude)]]
    points.push(parc)
  }
  return points
}


$("input[type=radio][name=delivery").click(elem => {
  if (elem.target.id == 'parcer_locker'){
      $('#map_parcel_locker').css('display', 'block')
  }
  else{
      $('#map_parcel_locker').css('display', 'none')
  }
})

$.ajax({
  type: "GET",
  url: "parcels/",
  success: function(objects){
    let points = parcels_array(objects)
    parcels_map(points)
  }
})


