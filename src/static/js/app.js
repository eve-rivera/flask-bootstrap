(function() {
    document.addEventListener("DOMContentLoaded", function(event) {
        console.log('Updating to current year.. :)')
        const currentYearSpan = document.getElementsByClassName("current-year");
        const date = new Date();
        currentYearSpan.item(0).innerHTML = "" + date.getFullYear();
    });
})();