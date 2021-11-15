// function to switch tabs
function handleTabs(evt, tabName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("tab-content");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" tab-active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " tab-active";
}

// function to toggle discussion replies
function toggleDiscussion(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-animate-opacity w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}

// function to toggle reply button
function toggleReply(id) {
    form = id + '-form'
    replyBtnId = 'reply-btn-' + id
    var replyBtn = document.getElementById(replyBtnId);
    var formElement = document.getElementById(form);

    // hide reply btn in main box
    if (replyBtn.className.indexOf("w3-hide") == -1) {
        replyBtn.className += " w3-hide";
    } else {
        replyBtn.className = replyBtn.className.replace(" w3-hide", "");
    }

    // show reply form
    if (formElement.className.indexOf("w3-show") == -1) {
        formElement.className += " w3-show";
    } else {
        formElement.className = formElement.className.replace(" w3-show", "");
    }
}

// toggle course contents
function handleCourseContent(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
        x.previousElementSibling.className =
            x.previousElementSibling.className.replace("w3-black", "w3-red");
    } else {
        x.className = x.className.replace(" w3-show", "");
        x.previousElementSibling.className =
            x.previousElementSibling.className.replace("w3-red", "w3-black");
    }
}