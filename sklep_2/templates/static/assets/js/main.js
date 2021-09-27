let slide = $('#grid_main_advertisement')
var number = Math.floor(Math.random()*4);

function hideSlide(){
    slide.fadeOut(500);
}

function slider(){
    number++;
    if(number>3){
        number = 0;
    }
    slide.html(`<img class="advertisement" src="{% static 'images/1.jpg' %}">`)
    slide.fadeIn(500);
    setTimeout("slider()", 5000)
    setTimeout("hideSlide()", 4500)
}
     
// window.onload = slider()


// " + number + "