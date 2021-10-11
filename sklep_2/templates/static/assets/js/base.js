let get_sidebar = document.querySelector('#toggle_bar')
let toggle = $('#toggle_grid')
let slid = document.querySelector('#carouselExampleCaptions')
let sidebar_status = true;
let input_search = $('#input_search')
var search_box = $('.search_box')
var search_list = $('#list_search_box')
var icon_cart = $('#cart_icon')
var shopping_cart = $('#shopping_cart_bar')


function getCookie(c_name) {
    if(document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if(c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if(c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
} 
function sidebar() {
    if (sidebar_status === true){
        get_sidebar.style.display = 'block';
        get_sidebar.style.opacity = '1';
        if($(window).width() < 1600){   
            slid.style.opacity = '0';
        } 
        toggle.html('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-caret-down" viewBox="0 0 16 16"><path d="M3.204 5h9.592L8 10.481 3.204 5zm-.753.659 4.796 5.48a1 1 0 0 0 1.506 0l4.796-5.48c.566-.647.106-1.659-.753-1.659H3.204a1 1 0 0 0-.753 1.659z"/></svg>')
        sidebar_status = false;
    }
    else {
        get_sidebar.style.display = 'none';
        get_sidebar.style.opacity = '0';
        if($(window).width() < 1600){
            slid.style.opacity = '1'
        }      
        toggle.html('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-caret-up" viewBox="0 0 16 16"><path d="M3.204 11h9.592L8 5.519 3.204 11zm-.753-.659 4.796-5.48a1 1 0 0 1 1.506 0l4.796 5.48c.566.647.106 1.659-.753 1.659H3.204a1 1 0 0 1-.753-1.659z"/></svg>')
        sidebar_status = true;
    }
}

function sendtext(text){
    $.ajax({
        type: "POST",
        url: "/search/",
        data: {
            'csrfmiddlewaretoken': getCookie("csrftoken"),
            'text': text,
        },
        success: function (list) {
            var array_products = ``
            for (i=0;i < list.data.length;i++){
                array_products += '<a href="' + list.data[i].url + '" class="list-group-item list-group-item-action " aria-current="true">' + list.data[i].name + '</a>'
            }
            search_list.html(array_products)
            
            
            
        }
    });
}

input_search.keyup(w => { 
    let words = w.target.value
    let len = parseInt(w.target.textLength)
    if (len > 0){
        search_box.addClass('active_search')
    }
    sendtext(words)

});

document.onclick = function (e) {
    if (e.target.id != 'input_search'){
        search_box.removeClass('active_search')
    }
    else{
        if (e.target.value != ''){
            search_box.addClass('active_search')
        }
        
    }
}

function cart_time(){
    shopping_cart.hover(function (){
        clearTimeout(a)
        }, 
        function(){  
            setTimeout(cart_shop, 300)
            })
    a = setTimeout(cart_shop, 1000)
    
    
 
}
function cart_shop(){
    shopping_cart.css('display', 'none')
    
}
icon_cart.hover(function () {
    shopping_cart.css('display', 'block')
    clearTimeout(a) 
    }, cart_time);




    