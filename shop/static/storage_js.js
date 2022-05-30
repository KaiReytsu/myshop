var page_num = 1;

document.addEventListener('DOMContentLoaded', 
    pages
)

function next_page(){
    page_num += 1;

    pages();
}
function prev_page(){
    page_num -= 1;
    pages();
}

function pages(){
    const csrftoken = document.querySelector(
        '[name=csrfmiddlewaretoken]'
    ).value;
    var prev = document.querySelector(
        '[name=prev]'
    );
    var next = document.querySelector(
        '[name=next]'
    );
    var page = document.getElementById(
        'page'
    );
    var last_page = parseInt(document.getElementById(
        'last_page'
    ).textContent);
    page.innerHTML = page_num;
    if (page_num >= 1 && page_num < last_page ){
        next.style.display = 'block';
    } else {
        next.style.display = 'none';
    }
    if (page_num > 1 && page_num <= last_page ){
        prev.style.display = 'block';
    } else{
        prev.style.display = 'none';
    }
    var post_body = JSON.stringify({
        'page': page_num
    });
    var request_headers = {
        'X-CSRFToken': csrftoken,
        'Accept': 'text/html',
        'Content-Type': 'application/json'
    };
    fetch(
        '/storage/',
        {
            method: 'POST',
            body: post_body,
            headers: request_headers
        }
    ).then(response => response.json()).then(response =>{
        var div = document.getElementById('items');
        div.innerHTML = '';
        
        for(var i of response.storage){
            var item_div = document.createElement('div');
            item_div.innerHTML = 
                i.product_name + 
                ' на складе в количестве ' + 
                i.stock + ' условных единиц'
            div.appendChild(item_div);
        }
        console.log(response)
    });

}