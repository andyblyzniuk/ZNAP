getUsers();
//getRate();
closeRate(1);
putAdmin(1,1);

function userRates(id) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://znap.pythonanywhere.com/api/v1.0/user/"+id+"/rate/", false);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send();
    uRates = JSON.parse(xhr.response);
    return uRates;
}

function getUsers(){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://znap.pythonanywhere.com/api/v1.0/user/", false);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send();
    users = JSON.parse(xhr.response);
    for (var i =users.length-1; i>=0; i--) {
        $('#list').append("<tr class='user'>" +
            "<th class='id' scope='row'></th>" +
            "<th class='name'></th>" +
            "<th class='middle_name'></th>" +
            "<th class='last_name'></th>" +
            "<th class='email'></th>" +
            "<th class='phone'></th>" +
            "<th class='rate'></th>" +
            "</tr>");
        console.log(users);
        id = users[i].id;
        first_name = users[i].first_name;
        last_name = users[i].last_name;
        middle_name = users[i].middle_name;
        email = users[i].email;
        phone = users[i].phone;

        uRates = userRates(id);

        hasRate = uRates.length > 0;

        console.log(hasRate);

        $('#list tr:last .id').append(id);
        $('#list tr:last .name').append(first_name);
        $('#list tr:last .middle_name').append(middle_name);
        $('#list tr:last .last_name').append(last_name);
        $('#list tr:last .email').append(email);
        $('#list tr:last .phone').append(phone);
        if (hasRate) {
            $('#list tr:last .rate').append('<button type="button" class="btn btn-primary active">Active Primary</button>');
        }
        else {
            $('#list tr:last .rate').append('no');
        }
    }

}

function getUser(id){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://znap.pythonanywhere.com/api/v1.0/user/"+id+"/", false);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send();
    user = JSON.parse(xhr.response);
    return user;
}

function getRate() {
  //  console.log(admin_id);
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://znap.pythonanywhere.com/api/v1.0/rate/", false);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send();
    rates = JSON.parse(xhr.response);
    console.log(rates);

    for (var i =rates.length-1; i>=0; i--){
        user = getUser(rates[i].user_id);
        console.log(user);
        first_name = user.first_name;
        last_name = user.last_name;
        middle_name = user.middle_name;

        
       $('#list2').append('<li class="list-group-item" xmlns="http://www.w3.org/1999/html">' +
            '<div class="row"> ' +
            '<div class="col-md-6"><h4 class="name"></h4><h6 class="description"></h6></div>' +
            '<div class="col-md-6 text-right"><h4 class="quality"></h4><h6 class="time"></h6></div>' +
            '</div>' +
            '</li>');

        $('#list2 li:last .name').append(first_name+' '+last_name);
        $('#list2 li:last .quality').append(rates[i].quality);
        //$('#list2 li:last .time').append(rates[i].dialog[0].timeStamp);
        $('#list2 li:last .description').append(rates[i].description);

        console.log(rates[i].description);
        console.log(rates[i].quality);
    }
}

function closeRate(id) {
    closeRate = {
        "is_closed" : true
    };

    var xhr = new XMLHttpRequest();
    xhr.open("PUT", "http://znap.pythonanywhere.com/api/v1.0/rate/"+id+"/", false);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(closeRate));
}


function putAdmin(admin_id, rate_id) {
    adminInRate = {
        admin: admin_id
    };
    var xhr = new XMLHttpRequest();
    xhr.open("PUT", "http://znap.pythonanywhere.com/api/v1.0/rate/"+rate_id+"/", false);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(adminInRate));

}