/**
 * Created by nebrasjemel on 11/29/15.
 */

// This is called with the results from from FB.getLoginStatus().
function statusChangeCallback(response) {
    console.log('statusChangeCallback');
    console.log(response);
    // Check Response Object
    if (response.status === 'connected') {
        postInfo(response.authResponse.accessToken);
    } else if (response.status === 'not_authorized') {
        // The person is logged into Facebook, but not your app.
        document.getElementById('status').innerHTML = 'Please log ' +
            'into this app.';
    } else {
        // The person is not logged into Facebook, so we're not sure if
        // they are logged into this app or not.
        document.getElementById('status').innerHTML = 'Please log ' +
            'into Facebook.';
    }
}

// This function is called when someone finishes with the Login
// Button.  See the onlogin handler attached to it in the sample
// code below.
function checkLoginState() {
    FB.getLoginStatus(function (response) {
        statusChangeCallback(response);
    });
}

window.fbAsyncInit = function () {
    FB.init({
        appId: '181450052202532',
        cookie: true,  // enable cookies to allow the server to access
                       // the session
        xfbml: true,  // parse social plugins on this page
        version: 'v2.5' // use version 2.5
    });

    // Now that we've initialized the JavaScript SDK, we call
    // FB.getLoginStatus().  This function gets the state of the
    // person visiting this page and can return one of three states to
    // the callback you provide.  They can be:
    //
    // 1. Logged into your app ('connected')
    // 2. Logged into Facebook, but not your app ('not_authorized')
    // 3. Not logged into Facebook and can't tell if they are logged into
    //    your app or not.
    //
    // These three cases are handled in the callback function.

    FB.getLoginStatus(function (response) {
        statusChangeCallback(response);
    });

};

// Load the SDK asynchronously
(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s);
    js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Here we run a very simple test of the Graph API after login is
// successful.  See statusChangeCallback() for when this call is made.
function postInfo(token) {
    console.log('Start ');
    FB.api('/me?fields=id,name', function (response) {
        console.log('Successful login for: ' + response);
        document.getElementById('status').innerHTML =
            'Thanks for logging in, ' + response.name + '! ';
        document.getElementById('status').innerHTML +=
            'Your last status: ' + response.posts.data[0].story;
        $.ajax({
            url: "/social", // the endpoint
            type: "POST", // http method
            data: {"userID": response.id, "account_name": response.name + " @Facebook", "access_token": token}, // data sent with the post request

            // handle a successful response
            success: function (json) {
                $('#emotion').text(format(json.result)); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
                update_lamp("192.168.1.106", "1ea00fa13605c157350bb6d53d8f1b6b", json.result)
            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#color').text('Success'); // remove the value from the input
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
}