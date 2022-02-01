    var links = document.querySelector(".site_links");
    var nav = document.querySelector(".navbar");
    if(nav){
        nav.addEventListener("click", function(e){
            if(links.style.display === 'block'){
                links.style.display = 'none';
            }else{
                links.style.display = 'block';
            }
        });
    }else{
       alert("nothing");
    }
    
    



