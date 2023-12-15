function validateLogin() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var errorMessageContainer = document.getElementById('error-message');
  
    // Clear previous error message
    errorMessageContainer.innerHTML = '';
  
    // Perform basic validation
    if (email === '' || password === '') {
      errorMessageContainer.innerHTML = 'Please enter both email and password.';
      return;
    }
  
    // Validate email format
    if (!isValidEmail(email)) {
      errorMessageContainer.innerHTML = 'Please enter a valid email address.';
      return;
    }

    
    window.location.href = 'RecDashboard/RecDashboard.html';
  }
  
  // Validator function for email format
  function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
  