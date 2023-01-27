//ex 1
// Instructions
// Create 2 variables, x and y. Each of them should have a different numeric value.
// Write an if/else statement that checks which number is bigger.
let x = 1;
let y = 3;
if (x > y){
    console.log(`${x} is the biggest number`)
} else {
    console.log(`${y} is the biggest number`)
}

// ex 2
// Instructions
// Create a variable called newDog where it’s value is “Chihuahua”.
// Check and display how many letters are in newDog.
// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
// Check if the variable newDog is equal to “Chihuahua”
// if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’

var newDog = 'Chihuahua';
// var newDog = 'banana';
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());
if (newDog == 'Chihuahua'){
    console.log(`I love Chihuahuas, it's my favorite dog breed`);
} else {
    console.log(`I dont care, I prefer cats`);
}
// ex 3
// Using the array above, console.log the number of users that are connected to the group chat based on the following rules:
// If there is no users (the users array is empty), console.log “no one is online”.
// If there is 1 user, console.log “<name_user> is online”.
// If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
// If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.

// let userNumber = prompt("Please enter a number:");
let userNumber = parseFloat(prompt("Please enter a number:"));
if (userNumber % 2 === 0){
    console.log(`${userNumber} is an even number`);
} else {
    console.log(`${userNumber} is an odd number`);
}
// ex 4
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
// const users = [];
if (users.length === 0) {
    console.log("No one is online");
  } else if (users.length === 1) {
    console.log(users[0] + " is online");
  } else if (users.length === 2) {
    console.log(users[0] + " and " + users[1] + " are online");
  } else {
    console.log(users[0] + ", " + users[1] + " and " + (users.length - 2) + " more are online");
  }
  