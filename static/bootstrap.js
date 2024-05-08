

// Go to next page via button click function
function nextPage(){
    window.location.href = '/filter';}
  
document.addEventListener('DOMContentLoaded', function () { 
    // Selecting all elements with data-bs-toggle="tooltip" 
    var tooltipElements = document.querySelectorAll('[data-bs-toggle="tooltip"]');  
         
    tooltipElements.forEach(function (element) {
        new bootstrap.Tooltip(element);});
    });

