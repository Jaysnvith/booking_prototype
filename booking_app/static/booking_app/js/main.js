$(document).ready(function() {

  // BURGER TOGGLE
  $(".navbar-burger").click(function() {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });


 // THEME TOGGLE
  if (localStorage.getItem('theme')) {
    $('html').attr('data-theme', localStorage.getItem('theme'));
  }
  
  $('#theme-toggle').click(function() {
    var currentTheme = $('html').attr('data-theme');
    if (currentTheme === 'light') {
      $('html').attr('data-theme', 'dark');
      localStorage.setItem('theme', 'dark');
    } else {
      $('html').attr('data-theme', 'light');
      localStorage.setItem('theme', 'light');
    }
  });

  // CANCEL BUTTON
  if (document.referrer) {
    $('#cancel-button').attr('href', document.referrer);
  } else {
    // If there's no referrer, set it to a default URL
    $('#cancel-button').attr('href', '/home');
  }

  // DELETE BUTTON
  document.getElementById('deleteButton').addEventListener('click', function() {
    var currentUrl = window.location.href;  // Get current URL
    var deleteUrl = currentUrl.replace('/update/', '/delete/');  // Modify URL for delete

    window.location.href = deleteUrl;  // Redirect to delete URL
  });
});
