function validateSignup() {
  var name = document.getElementById('name').value;
  var email = document.getElementById('email').value;
  var password = document.getElementById('password').value;
  var confirmPassword = document.getElementById('confirmPassword').value;
  var errorMessageContainer = document.getElementById('error-message');

  // Clear previous error message
  errorMessageContainer.innerHTML = '';

  // Perform basic validation
  if (name === '' || email === '' || password === '' || confirmPassword === '') {
    errorMessageContainer.innerHTML = 'Please fill in all fields.';
    return;
  }

  // Validate email format
  if (!isValidEmail(email)) {
    errorMessageContainer.innerHTML = 'Please enter a valid email address.';
    return;
  }

  // Validate name length
  if (name.length < 2) {
    errorMessageContainer.innerHTML = 'Name should be at least 2 characters long.';
    return;
  }

  // Perform password match validation
  if (password !== confirmPassword) {
    errorMessageContainer.innerHTML = 'Password and Confirm Password must match.';
    return;
  }
  
  window.location.href = 'RecLogin.html';
}

// Validator function for email format
function isValidEmail(email) {
  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}
