const maze = document.getElementById("maze");
const finish = document.getElementById("finish");
const player = document.getElementById("player");
const restartButton = document.getElementById("restart-button");

document.onkeydown = function(event) {
  switch (event.keyCode) {
    case 37:
      if (player.offsetLeft > 0) {
        player.style.left = player.offsetLeft - 20 + "px";
      }
      break;
    case 38:
      if (player.offsetTop > 0) {
        player.style.top = player.offsetTop - 20 + "px";
      }
      break;
    case 39:
      if (player.offsetLeft < maze.offsetWidth - player.offsetWidth) {
        player.style.left = player.offsetLeft + 20 + "px";
      }
      break;
    case 40:
      if (player.offsetTop < maze.offsetHeight - player.offsetHeight) {
        player.style.top = player.offsetTop + 20 + "px";
      }
      break;
  }
  if (
    player.offsetLeft == finish.offsetLeft &&
    player.offsetTop == finish.offsetTop
  ) {
    alert("You won!");
  }
};

restartButton.onclick = function() {
  player.style.top = "0px";
  player.style.left = "0px";
};
