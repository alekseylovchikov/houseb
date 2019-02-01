const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear().toString();

setTimeout(() => {
    $('#message').fadeOut('slow');
}, 5000);
