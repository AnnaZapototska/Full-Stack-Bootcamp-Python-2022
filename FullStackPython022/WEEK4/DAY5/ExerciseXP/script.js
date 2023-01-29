// ex 1
// Add the code above, to your HTML file

// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Change each first name of the two <ul>'s to your name.
// Delete the <li> that contains the text node “Sarah”.

// Bonus - Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

{/* <div id="container">Users:</div>
<ul class="list">
    <li>John</li>
    <li>Pete</li>
</ul>
<ul class="list">
    <li>David</li>
    <li>Sarah</li>
    <li>Dan</li>
</ul> */}

let container = document.getElementById("container");
console.log(container);



var listItems = document.getElementsByTagName("li");
// need to use loop  to find element Pete
for (var i = 0; i < listItems.length; i++) {
    if (listItems[i].textContent === "Pete") {
        listItems[i].textContent = "Richard";
    }
}
// have question how make changes 
var checkList = document.querySelectorAll("ul");
var listItem = document.querySelector("li:nth-child(1)"); 
var nameArr = listItem.textContent.split(' ');
nameArr[0] = "Anna";
listItem.textContent = nameArr.join(' ');

// var checkList = document.querySelectorAll("ul");
// for (var i = 0; i < checkList.length; i++) {
//     if (checkList[0].textContent) {
//         checkList[0].textContent = 'Anna'
//     }
// }


var checkItems = document.querySelectorAll("li");
for (var i = 0; i < checkItems.length; i++) {
    if (checkItems[i].textContent === "Sarah") {
        checkItems[i].parentNode.removeChild(checkItems[i]);
    }
}


var lists = document.querySelectorAll(".list");
for (var i = 0; i < lists.length; i++) {
    lists[i].classList.add("student_list");
}

var firstList = document.querySelector(".list");
firstList.classList.add("university", "attendance");

