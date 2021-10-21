function toggleVisibility(id) {
  var x = document.getElementById(id);
  // if (x.className.indexOf("w3-show") == -1) {
  //   x.className += " w3-show";
  // } else {
  //   x.className = x.className.replace(" w3-show", "");
  // }
  x.classList.toggle("w3-hide");
}

function toggleSideButton(id, buttonId){
  var childButtons=document.getElementById(buttonId).parentNode.children;
  for(let i of childButtons){
    i.classList.remove("w3-black");
  }
  var activeButton=document.getElementById(buttonId);
  activeButton.classList.add("w3-black");

  var childCards=document.getElementById(id).parentNode.children;
  var activeCard=document.getElementById(id);
  if(activeCard.classList.contains("w3-hide-medium")){
    for(let i of childCards){
      i.classList.add("w3-hide-medium");
      i.classList.add("w3-hide-large");
    }
    activeCard.classList.remove("w3-hide-medium");
    activeCard.classList.remove("w3-hide-large");
  }
}

// When the user scrolls the page, execute makeSticky
// window.onscroll = function() {makeSideNavSticky()};

// // Get the header
// var sidenav = document.getElementById("sidenav");
// var course_detail_card = document.getElementById("course-detail-card");

// // Get the offset position of the navbar
// var topOffset = sidenav.offsetTop-100;

// // Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
// function makeSideNavSticky() {
//   if (window.pageYOffset > topOffset) {
//     sidenav.classList.add("sticky");
//     // course_detail_card.classList.add("course-detail-card")
//   } else {
//     sidenav.classList.remove("sticky");
//     // course_detail_card.classList.remove("course-detail-card")
//   }
// } 