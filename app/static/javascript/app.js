/*jshint esversion: 6*/
// This application is for use with flas_many-to-many_model

// Event listeners
document.getElementById('userForm').addEventListener('submit', createUser);
document.getElementById('channelForm').addEventListener('submit', createChannel);

function showAlert(message, className) {
    const alert_div = document.createElement('div');
    // Pass in the className variable
    alert_div.className = `alert alert-${className}`;
    // Add the message
    alert_div.appendChild(document.createTextNode(message));
    // Insert the alert
    const page_title = document.getElementById('page-title');

    page_title.parentNode.insertBefore(alert_div, page_title);

    // Clear alert after 3 seconds
    setTimeout(() => document.querySelector('.alert').remove(), 3000);
}

function createUser(event) {
    // Prevent the normal form submission
    event.preventDefault();

    // Get the username supplied in the username input field
    let uname = document.getElementById('usernameInput').value;
    // Check for an empty input
    if (uname == '') {
        return showAlert('Username cannot be empty','danger')
    }
    // Clear the input
    document.getElementById('usernameInput').value = '';

    fetch('/adduser', {
        method: 'POST',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type': 'application/json'
        },
        body:JSON.stringify({'username': uname})
    })
    .then((res) => res.json())
    .then((data) => {
        if (data['error']) {
            showAlert(data['error'], 'danger')
        } else {
            showAlert(data['status'], 'dark')
        }
    }).catch((err) => console.log(err))
}

function createChannel(event) {
    // Prevent the normal form submission
    event.preventDefault();

    // Get the username supplied in the username input field
    let chan = document.getElementById('channelnameInput').value;
    // Check for an empty input
    if (chan == '') {
        return showAlert('Channel name cannot be empty','danger')
    }
    // Clear the input
    document.getElementById('channelnameInput').value = '';

    fetch('/addchannel', {
        method: 'POST',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type': 'application/json'
        },
        body:JSON.stringify({'channelname': chan})
    })
    .then((res) => res.json())
    .then((data) => {
        if (data['error']) {
            showAlert(data['error'], 'danger')
        } else {
            showAlert(data['status'], 'dark')
        }
    }).catch((err) => console.log(err))
}
