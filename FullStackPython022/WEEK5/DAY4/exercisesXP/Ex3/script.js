// Copy the code above, to a structured HTML file.
// In your Javascript file add the functionality which will allow you to drag the box and drop it into the target. Check out the Course Notes named DOM animations.

const animate = document.getElementById("box");
const target = document.getElementById("target");

let isDragging = false;
let currentX;
let currentY;
let initialX;
let initialY;
let xOffset = 0;
let yOffset = 0;

animate.addEventListener("mousedown", dragStart);
animate.addEventListener("mouseup", dragEnd);
animate.addEventListener("mouseout", dragEnd);
animate.addEventListener("mousemove", drag);

function dragStart(event) {
  initialX = event.clientX - xOffset;
  initialY = event.clientY - yOffset;

  isDragging = true;
}

function dragEnd(event) {
  initialX = currentX;
  initialY = currentY;

  isDragging = false;

  const animateRect = animate.getBoundingClientRect();
  const targetRect = target.getBoundingClientRect();

  if (
    animateRect.x > targetRect.x && animateRect.x < targetRect.x + targetRect.width 
    && animateRect.y > targetRect.y && animateRect.y < targetRect.y + targetRect.height
  ) {
    animate.style.backgroundColor = "green";
  } else {
    animate.style.backgroundColor = "red";
  }
}


function drag(event) {
  if (isDragging) {
    event.preventDefault();
    currentX = event.clientX - initialX;
    currentY = event.clientY - initialY;

    xOffset = currentX;
    yOffset = currentY;

    setTranslate(currentX, currentY, animate);
  }
}

function setTranslate(xPos, yPos, el) {
  el.style.transform = "translate3d(" + xPos + "px, " + yPos + "px, 0)";
}
