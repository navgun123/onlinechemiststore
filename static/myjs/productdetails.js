function getdata(data) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.response);
            console.log(output);
            table(output);
        }
    };
    xml.open('GET', 'showProductPhoto?search=' + data, true);
    xml.send();
}


function table(output) {
    var t = '';
    for (var i of output) {
        t += "<div class='pro-nav-thumb d-inline' onmouseover='photoget(" + JSON.stringify(i['photo']) + ")'>";
        t += "<img src='static/media/" + i['photo'] + "' alt='product-details' width='150' height='200'></div>";
    }
    document.getElementById('photo').innerHTML = t;
}

function photoget(data) {
    $('#bigphoto').attr({'src': 'static/media/' + data});
}


function sessionProduct(data) {
    // alert(document.getElementById('qty').value);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert("Items Added To Card Successfully");
            document.getElementById('cardsession').innerHTML = this.response;
        }
    };
    xmlhttp.open('GET', 'sessionProduct?q=' + data + '&qty=' + $('#qty').val(), true);
    xmlhttp.send()
}