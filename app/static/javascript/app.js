$(document).ready(function() {
    console.log('Document loaded');
    // Adding click event to login button
    $('#loginButton').on('click', function() {
        console.log('[*] Get token button clicked')
        // Grab the form values
        let auth_endpoint = $('#apiAuthEndpoint').val();
        console.log('[*] Authorization Endpoint: ' + auth_endpoint)

        let username = $('#username').val();
        console.log('[*] Username: ' + username)

        let password = $('#passwd').val();
        console.log('[*] Password: (not passing it through)')

        // Setup the request
        req = $.ajax({
            // The flask endpoint we'll trigger to actually send the request
            url: '/gettoken',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            // The data we want to send into flask
            data: JSON.stringify({
                'target': auth_endpoint,
                'username': username,
                'password': password
            })
        });

        console.log('This is after the ajax request');

        // After the call has finished, update the text in the token
        // display area in the html
        req.done(function(data) {
            $('#tokenresult').text(data.test_data);
        });

    });
});
