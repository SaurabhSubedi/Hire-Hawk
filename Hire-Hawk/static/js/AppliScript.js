document.getElementById('fileInputButton').addEventListener('click', function() {
    document.getElementById('fileInput').click();
  });
  
  document.getElementById('fileInput').addEventListener('change', function() {
    const selectedFile = this.files[0];
    if (selectedFile) {
      const fileName = selectedFile.name;
      alert(`Selected file: ${fileName}`);
      // You can add additional logic here to handle the selected file
    }

  });


  function redirectToAboutJob() {
    window.location.href = 'AboutJob.html';
  }

  function redirectToProfile() {
    window.location.href = 'ProfilePage.html';
  }
  