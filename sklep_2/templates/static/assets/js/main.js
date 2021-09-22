// let get_sidebar = $('.toggle_bar');
let get_sidebar = document.querySelector('.toggle_bar')
let toggle = $('#toggle_grid')
let sidebar_status = true;

function sidebar() {
    if (sidebar_status === true){
        get_sidebar.style.opacity = '1';
        toggle.html('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-caret-down" viewBox="0 0 16 16"><path d="M3.204 5h9.592L8 10.481 3.204 5zm-.753.659 4.796 5.48a1 1 0 0 0 1.506 0l4.796-5.48c.566-.647.106-1.659-.753-1.659H3.204a1 1 0 0 0-.753 1.659z"/></svg>')
        sidebar_status = false;
    }
    else {
        get_sidebar.style.opacity = '0';
        toggle.html('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-caret-up" viewBox="0 0 16 16"><path d="M3.204 11h9.592L8 5.519 3.204 11zm-.753-.659 4.796-5.48a1 1 0 0 1 1.506 0l4.796 5.48c.566.647.106 1.659-.753 1.659H3.204a1 1 0 0 1-.753-1.659z"/></svg>')
        sidebar_status = true;
    }
}