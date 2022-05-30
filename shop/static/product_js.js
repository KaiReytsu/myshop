

function savefunc(){
    const csrftoken = document.querySelector(
        '[name=csrfmiddlewaretoken]'
    ).value;
    var productname = document.querySelector(
        '[name=productname]'
        ).value;
    var price = document.querySelector(
        '[name=price]'
        ).value;
    var stock = document.querySelector(
            '[name=stock]'
        ).value;
    var post_body = JSON.stringify({
        'productname': productname,
        'price': price,
        'stock': stock
    });
    var request_headers = {
        'X-CSRFToken': csrftoken,
        'Accept': 'text/html',
        'Content-Type': 'application/json'
    };
    fetch(
        '/',
        {
            method: 'POST',
            body: post_body,
            headers: request_headers
        }
    ).then(response => console.log(response));
}