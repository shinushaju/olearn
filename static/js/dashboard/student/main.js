function w3_open() {
    document.getElementById("mySidebar").style.width = "100%";
    document.getElementById("mySidebar").style.display = "block";
}

function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
}

function handleDropDown(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}

function handleDropDownMenu() {
    var item = document.getElementById('menu-links');
    if (item.className.indexOf("w3-show") == -1) {
        item.className += " w3-show";
    } else {
        item.className = item.className.replace(" w3-show", "");
    }
}

function handleDropDownMenuMobile() {
    var mobileItem = document.getElementById('menu-mobile-links');
    if (mobileItem.className.indexOf("w3-show") == -1) {
        mobileItem.className += " w3-show";
    } else {
        mobileItem.className = mobileItem.className.replace(" w3-show", "");
    }
}

// code to change active class in navbar 

// Get the container element
var linksContainer = document.getElementById("nav");

// Get all buttons with class="btn" inside the container
var links = linksContainer.getElementsByClassName("side-nav-item");
// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < links.length; i++) {
    links[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("active");
        //console.log(current)
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}