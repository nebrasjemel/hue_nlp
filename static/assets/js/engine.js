/**
 * Created by nebrasjemel on 12/5/15.
 */


function format(str) {
    return str.replace(/\w\S*/g, function (txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
}

function update_lamp(ip_address, username, emotion) {

    function ajax_lamp(hue, bri, sat, number) {
        console.log("Lamp is updating : {\"bri\":" + bri + "\"sat\":" + sat + "\"hue\":' " + hue + "'}'") // sanity check
        $.ajax({
            url: "http://" + ip_address + "/api/" + username + "/lights/" + number + "/state", // the endpoint
            type: "PUT", // http method
            data: '{"bri":' + bri + ',"sat":' + sat + ',"hue":' + hue + '}', // data sent with the post request
            // handle a successful response
            success: function (json) {
                $('#color').text('Success'); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#color').text('Failure'); // remove the value from the input
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

    if (emotion != "none") {
        var bri = [0, 0, 0], hue = [0, 0, 0], sat = [0, 0, 0];
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

function get_emotion(status) {
    console.log("Classifying string") // sanity check
    $.ajax({
        url: "/classify", // the endpoint
        type: "POST", // http method
        data: {"status": status}, // data sent with the post request

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
};

$(document).ready(function () {
    setInterval(function () {
    }, 20000);

    $("#test2").click(function (e) {
        e.preventDefault();
        var value = $('#gotcha').val();
        console.log(value)
        get_emotion(value.toLowerCase());
    });
});

