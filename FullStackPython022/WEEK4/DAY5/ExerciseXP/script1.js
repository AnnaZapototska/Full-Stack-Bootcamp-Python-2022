// Instructions
// <div>Users:</div>
// <ul>
//     <li>John</li>
//     <li>Pete</li>
// </ul>


// Add the code above, to your HTML file
// Add a “light blue” background color and some padding to the <div>.
// Do not display the <li> that contains the text node “John”.
// Add a border to the <li> that contains the text node “Pete”.
// Change the font size of the whole body.
// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).

let colorDiv = document.querySelector("div").style.backgroundColor = "#ADD8E6";

var john = document.querySelector("li:first-child"); 
john.style.display = "none";

var pete = document.querySelector("li:last-child"); 
pete.style.border = "1px solid black";

let changeSize = document.querySelector("body").style.fontSize = "x-large";

