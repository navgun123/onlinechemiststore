function showcategory(category) {
    // alert(category);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.response);
            t = "";
            t += '<a href="#">Category</a>';
            t += '<ul class="dropdown">';
            // console.log(output);
            for (var i of output) {
                t += '<li class="has-children">';
                t += '<a href="#">' + i.catname + '</a>';
                t += '<ul class="dropdown">';
                for (var sb of i.sub) {
                    t += '<li><a href="shop?subid=' + sb.subid + '">' + sb.subname + '</a></li>';
                }
                t += '</ul></li>';
            }
            t += '</ul></li>';
            document.getElementById('navcatsub').innerHTML = t;
        }
    };
    xml.open('GET', 'navcategory', true);
    xml.send();
}

function searchmed() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.response);
            // alert(output);
            console.log(output);
            // document.getElementById('search').setAttribute('autocomplete',output);
            $('#search').autocomplete({
                source:output,
                minLength:2
            });
        }
    };
    xml.open('GET','searchmed',true);
    xml.send();
}


function showstores(store) {
     var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.response);
            t = "";
            t += '<a href="#">Store Nearby</a>';
            t += '<ul class="dropdown">';
            // console.log(output);
            for (var i of output) {
                t += '<li><a href="shop?storeemail=' + i.email + '">' + i.displayname + '</a></li>';
            }
            t += '</ul></li>';
            document.getElementById('navstore').innerHTML = t;
        }
    };
    xml.open('GET', 'navstore', true);
    xml.send();
}