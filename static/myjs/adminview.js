function deleteadmin(email) {
    alert(email);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert(this.responseText);
            window.location.href = 'adminview'
        }
    };
    xml.open('GET', 'adminDelete?email=' + email, true);
    xml.send()
}


function deletechemist(email) {
    alert(email);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert(this.responseText);
            window.location.href = 'chemistview'
        }
    };
    xml.open('GET', 'deletechemist?email=' + email, true);
    xml.send()
}

function updatemodel(data) {
    // alert(data);
    $('#email').val(data.email);
    $('#fname').val(data.fullname);
    $('#mobile').val(data.mobile);
    // $('#email').val(data.password);
    $('#updateadminmodel').modal('show');
}


function updateAdmin() {
    var controls = document.getElementById("myform").elements;
    var formdata = new FormData();
    for (var i = 0; i < controls.length; i++) {
        if (controls[i].type == "file") {
            formdata.append(controls[i].name, controls[i].files[0]);
        } else {
            formdata.append(controls[i].name, controls[i].value);
        }
    }
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert(this.responseText);
            $('#updateadminmodel').modal('hide');
            window.location.href = 'adminview';
        }
    };
    xml.open('POST', 'adminUpdate', true);
    xml.send(formdata)
}

function chemistupdatemodel(data) {
    $('#email').val(data.email)
    $('#dname').val(data.dname)
    $('#licensenumber').val(data.licensenumber)
    $('#state').val(data.state)
    $('#city').val(data.city)
    $('#address').val(data.address)
    $('#chemistupdatemodel').modal('show')
}




function chemistupdate() {
    var controls = document.getElementById("chemistupdate").elements;
    var formdata = new FormData();
    for (var i = 0; i < controls.length; i++) {
        if (controls[i].type == "file") {
            formdata.append(controls[i].name, controls[i].files[0]);
        } else {
            formdata.append(controls[i].name, controls[i].value);
        }
    }
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert(this.responseText);
            $('#chemistupdatemodel').modal('hide');
            window.location.href = 'chemistview';
        }
    };
    xml.open('POST', 'chemistupdate', true);
    xml.send(formdata)
}
