/*jshint esversion: 6*/
// This application is for use with flas_many-to-many_model

// Event listener for Create User
document.getElementById('userForm').addEventListener('submit', createUser);

function getFormUserName() {
    return document.getElementById('usernameInput').value;
}

function createUser(event) {
    // Prevent the normal form submission
    event.preventDefault();

    // Get the username supplied in the username input field
    let uname = document.getElementById('usernameInput').value;

    fetch('/adduser', {
        method: 'POST',
        headers: new Headers(),
        body:JSON.stringify({'username': uname})
    })
    .then((res) => {
        let response = res.json();
        console.log(response);
    })
    .catch((err) => console.log(err))
}

document.getElementById('createChannelBtn').addEventListener('click', getChanName)

function getChanName() {
    let channelName = document.getElementById('channelnameInput').value;
    console.log(channelName);
}
