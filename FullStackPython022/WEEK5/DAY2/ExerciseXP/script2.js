//ex 3

// In the JS file:
// Declare a global variable named allBoldItems.
// Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
// Create a function called highlight() that changes the color of all the bold text to blue.
// Create a function called return_normal() that changes the color of all the bold text back to black.
// Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() on mouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example

// let allBoldItems =[];
// let paragraph = document.getElementById('paragraph');
// paragraph.addEventListener("mouseover", highlight);
// paragraph.addEventListener("mouseout", return_normal);
// function getBold_items(){
//     allBoldItems = document.getElementsByTagName('strong'); 
    
// }
// function highlight() {
//     getBold_items()
//     for (let item of allBoldItems) {
//       item.style.color = "blue";
//     }
//   }
  
//   function return_normal() {
//     getBold_items()
//     for (let item of allBoldItems) {
//       item.style.color = "black";
//     }
//   }


//ex 4
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:
// function volume_sphere()
//  {
//   var volume;
//   var radius = document.getElementById('radius').value;
//   radius = Math.abs(radius);
//   volume = (4/3) * Math.PI * Math.pow(radius, 3);
//   volume = volume.toFixed(4);
//   document.getElementById('volume').value = volume;
//   return false;
//  } 
// window.onload = document.getElementById('MyForm').onsubmit = volume_sphere;


// ex 5
// Add many events listeners to one element on your webpage. Use the click, mouseover, mouseout and dblclick events.
// Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.


const element = document.getElementById('element');

element.addEventListener('mouseover', mouseoverElement);
element.addEventListener('mouseout', mouseoutElement);
element.addEventListener('click', clickElement);
element.addEventListener('dblclick', dblclickrElement);

function mouseoutElement(){
    element.style.width = '350px';   
    element.style.height = '60px'; 
};
function mouseoverElement(){
    element.style.width = '150px';   
    element.style.height = '30px'; 
};
function clickElement(){
    element.style.backgroundColor = 'red'; 
};

function dblclickrElement(){
   element.innerHTML += "Hello World ";
};

const elementSecond = document.getElementById('elementSecond');

elementSecond.addEventListener('mouseover', mouseoverelementSecond);
elementSecond.addEventListener('mouseout', mouseoutelementSecond);
elementSecond.addEventListener('click', clickelementSecond);
elementSecond.addEventListener('dblclick', dblclickrelementSecond);

function mouseoverelementSecond(){
    elementSecond.style.width = '50px';   
    elementSecond.style.height = '50px'; 
};
function mouseoutelementSecond(){
    elementSecond.style.width = '150px';   
    elementSecond.style.height = '30px'; 
};
function clickelementSecond(){
    elementSecond.style.backgroundColor = 'red'; 
};

function dblclickrelementSecond(){
    elementSecond.style.backgroundColor = 'green'; 
};