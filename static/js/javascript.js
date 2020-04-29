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
var dateTime = '<div class="small-text text-light mr-2"><i class="fas fa-calendar-day small-text text-secondary"></i> ' + date + ' <i class="far ml-2 fa-clock small-text text-secondary"></i> ' + time + '</div>';

$('#current-date').append(dateTime);


// menu animation

$('.add-button').on('click', function() {
    if ($('.add-button').hasClass('add-button-open')) {
        $('.add-button').addClass('add-button-close')
        $('.add-button').removeClass('add-button-open')

        $('.add-food').addClass('add-food-close')
        $('.add-food').removeClass('add-food-open')

        $('.add-wrapper').addClass('menu-container-close')
        $('.add-wrapper').removeClass('menu-container-open')

        $('.add-home').addClass('add-home-close')
        $('.add-home').removeClass('add-home-open')
    } else {
        $('.add-button').removeClass('add-button-close')
        $('.add-button').addClass('add-button-open')
        
        $('.add-food').removeClass('add-food-close')
        $('.add-food').addClass('add-food-open')
        
        $('.add-wrapper').removeClass('menu-container-close')
        $('.add-wrapper').addClass('menu-container-open')
        
        $('.add-home').removeClass('add-home-close')
        $('.add-home').addClass('add-home-open')
    }
    if ($('.add-shopping').hasClass('shopping-open')) {
        $('.add-shopping').addClass('shopping-close')
        $('.add-shopping').removeClass('shopping-open')

        $('.add-dinner').addClass('dinner-close')
        $('.add-dinner').removeClass('dinner-open')
    }
});

$('.add-home').on('click', function() {
    if ($('.add-shopping').hasClass('shopping-open')) {
        $('.add-shopping').addClass('shopping-close')
        $('.add-shopping').removeClass('shopping-open')

        $('.add-dinner').addClass('dinner-close')
        $('.add-dinner').removeClass('dinner-open')
    } else {
        $('.add-shopping').removeClass('shopping-close')
        $('.add-shopping').addClass('shopping-open')

        $('.add-dinner').addClass('dinner-open')
        $('.add-dinner').removeClass('dinner-close')
    }
});