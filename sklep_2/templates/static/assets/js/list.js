function list_filter_button(){
    console.log($("#list_filter").is(':visible'));
    if($("#list_filter").is(':visible')){
        $("#list_filter").css('display', 'none')
    }
    else{
        $("#list_filter").css('display', 'block')
    }
    
    }