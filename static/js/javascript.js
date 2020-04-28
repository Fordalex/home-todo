function formatMinutes() {
    var mins = today.getMinutes()
    if (mins < 10) {
        mins = '0' + mins
    }
    return mins
}

function formatHour() {
    var hour = today.getHours()
    if (hour > 12) {
        hour = hour - 12
    }
    if (hour < 10) {
        hour = '0' + hour
    }
    return hour
}

var today = new Date();
var date = today.getDate() + '/' + (today.getMonth()+1) + '/' + today.getFullYear();
var minutes = formatMinutes();
var hours = formatHour();
var time = hours + ":" + minutes;
var dateTime = date+' '+time;

$('#current-date').append(dateTime);


// menu animation

$('.add-button').on('click', function() {
    $('.add-button').toggleClass('add-button-close')
    $('.add-button').toggleClass('add-button-open')
    $('.add-food').toggleClass('add-food-open')
    $('.add-food').toggleClass('add-food-close')
    $('.add-wrapper').toggleClass('menu-container-close')
    $('.add-wrapper').toggleClass('menu-container-open')
    $('.add-home').toggleClass('add-home-close')
    $('.add-home').toggleClass('add-home-open')

});