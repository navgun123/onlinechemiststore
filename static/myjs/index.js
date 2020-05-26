function getdata(find) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.response);
            console.log(output);
            card(output);
        }
    };
    xml.open('GET', 'showProduct?search=' + find, true);
    xml.send();
}


function card(output) {
    var t = '';
    for (var i of output) {
        t += '<div class="card-deck m-2 d-inline-flex" style="width: 20rem">';
        t += '<div class="card">';
        t += '<a href="productDescription?pid=' + i.pid + '" style="text-decoration: none" class="text-dark">';
        t += '<img class="card-img-top" style="width: 400px;height: 250px" src="static/media/' + i['productimage'] + '" alt="Card image cap">';
        t += '<div class="card-body">';
        t += '<div class="card-text text-center text-uppercase">' + i.productname + '</div>';
        t += '<div class="text-center badge-pill bg-warning">offer</div>';
        t += '<p class="text-center">&#8377;&nbsp;<strike>' + i.productprice + '</strike>&nbsp;&nbsp;&nbsp;' + i.productdiscount + '%<span id="pdiscount"></span></p></div></a>';
        t += '<div class="card-footer text-center">';
        if (i.productdiscount > 0) {
            t += '<button onclick="sessionProduct(' + i.pid + ')" class="btn-carts">Add To Card</button>';
        } else {
            t += '<button class="btn-carts">Out of Stock</button>';
        }
        t += '</div></div></div>'
    }
    document.getElementById('cat').innerHTML = t;
}


function getCategory(data) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.response);
            // console.log(output);
            var t = '';
            for (var i of output) {
                t += '<option value="' + i.subid + '">' + i.subname + '</option>'
            }
            document.getElementById('subcattbody').innerHTML = t;
            $('#subcatgory').slideDown(1000);
        }
    };
    xml.open('GET', 'filterSubCat?cat=' + data, true);
    xml.send();
}

function sessionProduct(data) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('cardsession').innerHTML = this.response;
        }
    };
    xmlhttp.open('GET', 'sessionProduct?q=' + data, true);
    xmlhttp.send()
}