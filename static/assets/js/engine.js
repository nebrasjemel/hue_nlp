/**
 * Created by nebrasjemel on 12/5/15.
 */


// formats a string such that it takes everything to lowercase except for the 
// first letter, just to make it look nice
function format(str) {
    return str.replace(/\w\S*/g, function(txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
}

// this function updates the lamp by issuing PUT request and using 
// Ajax to continuously get user statuses without reloading the page
function update_lamp(ip_address, username, emotion) {
    function ajax_lamp(hue, bri, sat, number) {
        console.log("Lamp is updating : {\"bri\":" + bri + "\"sat\":" + sat + "\"hue\":' " + hue + "'}'") // sanity check
        $.ajax({
            url: "http://" + ip_address + "/api/" + username + "/lights/" + number + "/state", // the endpoint
            type: "PUT", // http method
            data: '{"bri":' + bri + ',"sat":' + sat + ',"hue":' + hue + '}', // data sent with the post request
            // handle a successful response
            success: function(json) {
                $('#color').text('Success'); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
            },

            // handle a non-successful response
            error: function(xhr, errmsg, err) {
                $('#color').text('Failure'); // remove the value from the input
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }
    // if the user's text doesn't suggest any emotion, we set everything to 0
    if (emotion != "none") {
        var bri = [0, 0, 0],
            hue = [0, 0, 0],
            sat = [0, 0, 0];
        // in all the other cases, we output the light coor, brightness and
        // saturation that we've seen it is associated with those feelings
        if (emotion == "sadness") {
            bri = [254, 150, 150];
            hue = [49342, 23862, 43717];
            sat = [241, 251, 251];
        }
        else if (emotion == "joy") {
            bri = [130, 254, 254];
            hue = [49342, 25718, 23445];
            sat = [241, 254, 251];
        }
        else if (emotion == "disgust") {
            bri = [101, 116, 149];
            hue = [55889, 3604, 58315];
            sat = [230, 181, 161];
        }
        else if (emotion == "trust") {
            bri = [101, 116, 149];
            hue = [40823, 34172, 46341];
            sat = [251, 152, 250];
        }
        else if (emotion == "anger") {
            bri = [254, 254, 254];
            hue = [49342, 43412, 46329];
            sat = [241, 252, 251];
        }
        else if (emotion == "surprise") {
            bri = [254, 254, 254];
            hue = [14630, 65335, 64440];
            sat = [190, 236, 253];
        }
        for (var i = 1; i < 4; i++) {
            ajax_lamp(hue[i - 1], bri[i - 1], sat[i - 1], i);
        }
    }
};

// as it says, the function gets emotion from a status
function get_emotion(status) {
    console.log($("#related_account").val());
    var obj=$("#related_account").val().split(":");
    console.log("Classifying string") // sanity check
    var ip_address = $('#ip_address').text()
    $.ajax({
        url: "/classify", // the endpoint
        type: "POST", // http method
        data: {
            "status": status
        }, // data sent with the post request

        // handle a successful response
        success: function(json) {
            $('#emotion').text(format(json.result)); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            update_lamp(obj[0], obj[1], json.result)
        },

        // handle a non-successful response
        error: function(xhr, errmsg, err) {
            console.log("failure"); // remove the value from the input
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

// check if the document is ready
$(document).ready(function() {
    // runc checks if the app is still running
    var run = false;
    $("#run").click(function(e) {
        e.preventDefault();
        run = true;
        $("#choice").hide(400);
        $("#engine").show(700);
    });
    setInterval(function() {
        if (run == true) {
            FB.api('/me?fields=id,name,posts', function(response) {
                var i = 0;
                while (!response.posts.data[i].message) {
                    i++;
                }
                var value = response.posts.data[i].message;
                console.log(value);
                $('#status').text(value);
                get_emotion(value.toLowerCase());
            });
        }
    }, 5000);
});