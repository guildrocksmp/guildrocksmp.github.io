// Add a class to the body element when the user starts scrolling
window.addEventListener('scroll', function() {
    document.body.classList.add('scrolling');
  });
  
  // Remove the class from the body element when the scrolling stops
  var timeout;
  window.addEventListener('scroll', function() {
    clearTimeout(timeout);
    timeout = setTimeout(function() {
      document.body.classList.remove('scrolling');
    }, 100);
  });