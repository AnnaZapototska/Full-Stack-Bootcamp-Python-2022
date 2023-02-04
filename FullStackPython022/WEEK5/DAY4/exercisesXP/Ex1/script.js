// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.

function sayHelloWorld() {
    alert( 'Hello World!' );
  }
  
  setTimeout(sayHelloWorld, 2000);


// Part II
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
let containerParam = document.getElementById('container');
function addParam() {
    const newParagraph = document.createElement("p");
    newParagraph.innerHTML = "Hello World";
    container.appendChild(newParagraph);
  }
  
  setTimeout(addParam, 2000);

// Part III
// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.

let count = 0;

const intervalId = setInterval(() => {
  count++;
  const newParagraphS = document.createElement("p");
  newParagraphS.innerHTML = "Hello World";
  container.appendChild(newParagraphS);

  if (count === 5) {
    clearInterval(intervalId);
  }
}, 2000);

const stopButton = document.getElementById("clear");
stopButton.addEventListener("click", () => {
  clearInterval(intervalId);
});
