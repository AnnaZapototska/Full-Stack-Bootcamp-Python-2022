// ex

const form = document.querySelector("#libform");
const shuffleButton = document.querySelector("#lib-button");
let click = 0; 
  form.addEventListener("submit", function(event) {
    event.preventDefault();
    const noun = document.querySelector("#noun").value;
    const adjective = document.querySelector("#adjective").value;
    const person = document.querySelector("#person").value;
    const verb = document.querySelector("#verb").value;
    const place = document.querySelector("#place").value;
    
    if (!noun || !adjective || !person || !verb || !place) {
      console.error("All fields are required");
      return;
    }
    const story = `${noun} ${adjective} ${person} ${verb} ${place}`
    const storyElement = document.querySelector("#story");
    storyElement.innerHTML = story;
   
  });

