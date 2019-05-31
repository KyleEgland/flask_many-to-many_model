// User editing modal
// This code was adapted fromm the example on the bootstrap website
// This is an event listener for the modal display call
$('#userEditModal').on('show.bs.modal', modalDisplay);
$('#usernameUpdateForm').submit(userUpdate);

function modalDisplay(event) {
    event.preventDefault();
    // Button that triggered the modal
    var button = $(event.relatedTarget);
    // Extract info from data-* attributes
    var username = button.data('username');
    // Update the modal's content. We'll use jQuery here, but you could use a
    // data binding library or other methods instead.
    var modal = $(this);
    modal.find('.modal-title').text('Edit User: ' + username);
    modal.find('.modal-body .form-group input').val(username);
}

function userUpdate(event) {
    event.preventDefault();
}
