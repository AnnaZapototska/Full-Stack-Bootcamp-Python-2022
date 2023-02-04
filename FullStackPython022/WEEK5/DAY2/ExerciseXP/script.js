//ex 1
// Using a DOM property, retrieve the h1 and console.log it.
// Using DOM methods, remove the last paragraph in the <article> tag.
// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

// let paramH = document.getElementsByTagName("h1");
// console.log(paramH);

// let elementDelete = document.querySelector('p:last-child');
// elementDelete.parentElement.removeChild(elementDelete);

// let h2 = document.querySelector('h2');
// h2.addEventListener('click', onClickH2);
// function onClickH2() {
//     this.style.backgroundColor = 'red';    
// }
// h2.addEventListener('click', onMouseOverH2);
// function onMouseOverH2() {
//     this.style.fontSize = `${Math.floor(Math.random() * 101)}px`;
// }

// let h3 = document.querySelector('h3');
// h3.addEventListener('click', onClickH3);
// function onClickH3() {
//     this.style.display = "none";    
// }

// let article = document.querySelector('article');
// let button = document.querySelector('button');
// button.addEventListener('click', onClickButton);
// function onClickButton() {
//     article.style.fontWeight = 'bold';    
// }
// let hideParagraph = document.getElementById('hideParagraph');
// console.log(hideParagraph);
// hideParagraph.addEventListener("mouseover", function() {
//     hideParagraph.style.opacity = 0;
//   });

  
// ex 2

// Retrieve the form and console.log it.
// Retrieve the inputs by their id and console.log them.
// Retrieve the inputs by their name attribute and console.log them.
// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.

let form = document.forms[0];
let fname = form.elements.fname;
let lname = form.elements.lname;
console.log(form);

console.log(document.getElementById('fname'), document.getElementById('lname'));
console.log(document.getElementsByName('fname'), document.getElementsByName('lname'));
console.log(fname, lname);

form.addEventListener('submit', submitForm);

function submitForm(event) {
    if (!fname.value || !lname.value ) {
        alert('Enter text!');
        return;
    }    
    let ulElements = document.querySelector('.usersAnswer');
    let liFname = document.createElement('li');
    let liLname = document.createElement('li');  
    liFname.innerHTML = fname.value;
    liLname.innerHTML = lname.value;
    ulElements.appendChild(liFname);
    ulElements.appendChild(liLname);
    event.preventDefault();
}

