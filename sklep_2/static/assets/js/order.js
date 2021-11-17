


$("input[type=radio][name=delivery").click(elem => {
    if (elem.target.id == 'parcer_locker'){
        $('#map_parcel_locker').css('display', 'block')
    }
    else{
        $('#map_parcel_locker').css('display', 'none')
    }
})


var m = L.map('map_parcel_locker').setView([52.012, 18.922], 6)
  
// L.control.addTo(m);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png?').addTo(m)

points = [
    ['Warsaw', [52.241333, 21.028198]],
    ['Gdansk', [54.349722, 18.648001]],
    ['Cracow', [50.055142, 19.934230]],
]

for(i=0; i<points.length; i++){
    console.log(i);
    L.marker(points[i][1]).addTo(m).bindPopup(points[i][0]);
}
 
