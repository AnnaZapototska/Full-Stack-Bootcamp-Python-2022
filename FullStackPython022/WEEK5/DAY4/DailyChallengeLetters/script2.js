const nameInput = document.getElementById("nameInput");

nameInput.addEventListener("input", function(event) {
  const value = event.target.value;
  const lettersOnly = value.replace(/[^a-zA-Z]/g, "");
  event.target.value = lettersOnly;
});
